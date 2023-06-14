import requests
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def initiate_payment(request):
    if request.method == "POST":
        email = request.POST.get("email")
        amount = 550000
        paystack_url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "email": email,
            "amount": amount,
            "callback_url": request.build_absolute_uri(reverse("paystack_callback")),
        }
        response = requests.post(paystack_url, headers=headers, json=data)
        response_json = response.json()
        if "data" in response_json:
            authorization_url = response_json["data"].get("authorization_url")
            if authorization_url:
                return HttpResponseRedirect(authorization_url)

    return render(request, "initiate_payment.html")


def paystack_callback(request):
    reference = request.GET.get("reference")
    paystack_url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }
    # Use the transaction reference returned by Paystack to verify the payment status
    response = requests.get(paystack_url, headers=headers)
    response_json = response.json()
    if response_json["data"]["status"] == "success":
        # Payment was successful, process the order
        # Update the user's has_paid status to True
        user = request.user
        user.has_paid = True
        user.save()
        return redirect('dashboard')
    else:
        # Payment failed or was not successful
        return HttpResponse("Payment failed.")
