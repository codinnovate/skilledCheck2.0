from django.contrib.auth import login as auth_login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, View, ListView, DetailView, TemplateView
from .form import ClientSignUpForm,FreelancerSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Freelancer, Client
from django.contrib.auth.models import  auth

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .mixins import MessaHandler
import random

# def login(client: Client, user: User) -> None:
#     user_logged_in.disconnect(receiver=update_last_login)
#     client.force_login(user=user)
#     user_logged_in.connect(receiver=update_last_login)


def login_view_freelancer(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        freelancer = Freelancer.objects.filter(phone_number = phone_number)
        if not freelancer.exists():
            messages.info(request, 'Phone Number does not Exist !')
        for object in freelancer:
            object.otp = random.randint(1000, 9999)
            object.save()
            message_handler = MessaHandler(phone_number, object.otp ).send_otp()
            return redirect(f'otp/{object.uid}')

    return render(request, 'login.html')


# def login_view_client(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         client = Client.objects.filter(phone_number = phone_number)
#         if not client.exists():
#             messages.info(request, 'Phone Number does not Exist !')
#         for object in client:
#             object.otp = random.randint(1000, 9999)
#             object.save()
#             message_handler = MessaHandler(phone_number, object.otp ).send_otp()
#             return redirect(f'otp/{object.uid}')

#     return render(request, 'login.html')


def payment(request):
    return render(request, 'payment.html')
 
def register(request):
    return render(request, 'register.html')

    
def user_login(request):
    return render(request, 'logintype.html')


class client_register(CreateView):
    model = User 
    form_class = ClientSignUpForm
    template_name = 'client.html'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('/')


class freelancer_register(CreateView):
    model = User
    form_class = FreelancerSignUpForm
    template_name = 'freelancer.html'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('share')







def logout_view(request):
    logout(request)
    return redirect('/')

def otp_freelancer(request, uid):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        freelancer = Freelancer.objects.get(uid=uid)
        if otp == freelancer.otp:
            auth_login(request, freelancer.user)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Incorrect OTP code !')
            # return redirect(f'otp/{uid}')
            return redirect('.')
    return render(request, 'otp.html')

# def otp_client(request, uid):
#     if request.method == 'POST':
#         otp = request.POST.get('otp')
#         client = Client.objects.get(uid=uid)
#         if otp == client.otp:
#             login(request, client.user)
#             return redirect('/dashboard')
#         else:
#             messages.info(request, 'Incorrect OTP code !')
#         return redirect(f'otp/{uid}')
#     return render(request, 'otp.html')


class FreelancerList(ListView):
    model = Freelancer
    template_name = 'explore.html'

class FreelancerDetail(DetailView):
    model = Freelancer
    template_name = 'singleuser.html'

class Referothers(TemplateView):
    template_name = 'share.html'