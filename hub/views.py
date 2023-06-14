from django.shortcuts import render
from django.core.mail import send_mail
from accounts.decorators import payment_required  # ← new
from django.contrib.auth.decorators import login_required
from accounts.models import Freelancer, User
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReceiptForm
from .models import Receipt
# from weasyprint import HTML



from django.shortcuts import render
from .forms import ReceiptForm

def generate_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            # Get the form data
            name = form.cleaned_data['name']
            # product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            total = quantity * price
            # date = form.cleaned_data['date']
            # receipt_number = form.cleaned_data['receipt_number']
            # payment_method = form.cleaned_data['payment_method']
            # amount_paid = form.cleaned_data['amount_paid']
            # change = form.cleaned_data['change']

            # Prepare the context data for the template
            context = {
                'name':'name',
                # 'product': product,
                'quantity': quantity,
                'price': price,
                'total': total,
            #     'date': date,
            #     'receipt_number': receipt_number,
            #     'payment_method': payment_method,
            #     'amount_paid': amount_paid,
            #     'change': change,
             }
            receipt = Receipt(name=name, price=price, quantity=quantity)
            receipt.save()
            html = render(request, 'receipt.html', {'receipt': receipt})
            pdf_file = HTML(string=html).write_pdf()
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'filename="receipt.pdf"'
            return response
            
            # return render(request, 'receipt.html', context)

    else:
        form = ReceiptForm()

    # Render the form template
    return render(request, 'generate_receipt.html', {'form': form})




# def generate_receipt_pdf(request):
#     if request.method == 'POST':
#         form = ReceiptForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             price = form.cleaned_data['price']
#             quantity = form.cleaned_data['quantity']
#             total = quantity * price


#             # Save the receipt to the database
#             p = canvas.Canvas(response)

#             p.setFont("Helvetica-Bold", 16)
#             p.drawString(50, 750, "Receipt")

#             p.setFont("Helvetica-Bold", 12)
#             p.drawString(50, 700, f"Product Name: {name}")
#             p.drawString(50, 680, f"Price: {price}")
#             p.drawString(50, 660, f"Quantity: {quantity}")
#             p.drawString(50, 640, f"Total: {receipt.total}")

#             p.showPage()
#             p.save()

#             return response
#     else:
#         form = ReceiptForm()

#     return render(request, 'generate_receipt.html', {'form': form})


# @login_required
# @verification_required 
def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        sender_name = request.POST['SenderName']
        sender_email = request.POST['SenderEmail']
        message = request.POST['message']

        send_mail(
            'Artisan Needed From ' + sender_name ,
            message,
            sender_email,
            ['skilledcheck@gmail.com'],
        )
        return render(request, 'home.html', {'sender_name'})

    else:
        return render(request, 'home.html', {}) 

@login_required
def Dashboard(request):
    freelancer = Freelancer.objects.get(user=request.user)
    context = {'freelancer': freelancer}
    return render(request, 'dashboard.html', context)      



def privacy(request):
    return render(request, 'privacy.html')