import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import PaymentForm
from .models import Payment


def initiate_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            email = payment_form.cleaned_data.get("email")
            amount = payment_form.cleaned_data.get("amount")
            paystack_url = "https://api.paystack.co/transaction/initialize"
            headers = {
                "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
                "Content-Type": "application/json",
            }
            data = {
                "email": email,
                "amount": amount * 100,  # Paystack uses kobo as the currency unit
                "callback_url": request.build_absolute_uri(reverse("paystack_callback")),
            }
            response = requests.post(paystack_url, headers=headers, json=data)
            response_json = response.json()
            return HttpResponseRedirect(response_json["data"]["authorization_url"])
    else:
        payment_form = PaymentForm()

    return render(request, "initiate_payment.html", {"payment_form": payment_form})


def paystack_callback(request):
    reference = request.GET.get("reference")
    paystack_url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }
    response = requests.get(paystack_url, headers=headers)
    response_json = response.json()
    if response_json["data"]["status"] == "success":
        # Payment was successful, process the order
        payment = get_object_or_404(Payment, ref=reference)
        payment.status = Payment.SUCCESS
        payment.save()
        user = payment.user
        user.has_paid = True
        user.save()
        messages.success(request, f"Payment completed successfully, NGN {payment.amount}.")
   
