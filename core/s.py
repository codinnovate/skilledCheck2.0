# from django.shortcuts import get_object_or_404, render, redirect
# from django.http.request import HttpRequest
# from django.http.response import HttpResponse
# from django.urls import reverse
# from django.contrib import messages
# from django.conf import settings
# from .forms import PaymentForm
# from .models import Payment
# import paystack
# from accounts.models import User


# # def initiate_payment(request):
# #     amount = 55000
# #     email = User.email
# #     reference = paystack.transaction.initialize(amount=amount, email=email)['data']['reference']  # generate a unique reference for the transaction
# #     return redirect('verify_payment', reference=reference)

# def initiate_payment(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         payment_form = PaymentForm(request.POST)
#         if payment_form.is_valid():
#             payment: Payment = payment_form.save(commit=False)
#             payment.user_id = request.user.id  # set the user_id field explicitly
#             payment.save()
            
#             return render(request, 'make_payment.html', {'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
#     else:
#         payment_form = PaymentForm()
#     return render(request, "initiate_payment.html", {"payment_form": payment_form,},)



# def generate_paystack_url(payment):
#     ref = payment.reference
#     verify_url = reverse('verify-payment', args=[ref])

# def verify_payment(request, ref: str):
#     trxref = request.GET["trxref"]
#     if trxref != ref:
#         messages.error(
#             request,
#             "The transaction reference passed was different from the actual reference. Please do not modify data during transactions",
#         )
#     payment: Payment = get_object_or_404(Payment, ref=ref)
#     if payment.verify_payment():
#         user = User.objects.get(id=request.user.id)
#         user.has_paid = True
#         user.save()
#         messages.success(
#             request, f"Payment Completed Successfully, NGN {payment.amount}."
#         )
#         messages.success(
#             request, f"Your Account has been Activated Successfully"
#         )
#     else:
#         messages.warning(request, "Sorry, your payment could not be confirmed.")
#         return redirect("initiate-payment")
    
    
# # def verify_payment(request, reference):
# #       transaction_details = paystack.transaction.verify(reference)  # verify the transaction with the reference
# #       if transaction_details['data']['status'] == 'success':
# #             user = User.objects.get(username=request.user.username)
# #             user.has_paid = True
# #             user.save()
# #             return render(request, 'payment_confirmation.html', {'transaction_details': transaction_details})
# #       else:
# #             return render(request, 'payment_failed.html')
        