from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Client,Freelancer, LGA_CHOICES, STATE_CHOICES, GENDER_CHOICES, QUALIFICATION_CHOICES, BANK_CHOICES, Lang_choice
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget

class ClientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField()
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    home_address = forms.CharField(required=True)
    state = forms.ChoiceField( choices=STATE_CHOICES)
    lga = forms.ChoiceField(choices=LGA_CHOICES)
    city = forms.CharField(max_length=200)
    gender = forms.ChoiceField( choices=GENDER_CHOICES)
    language_spoken = forms.CharField(max_length = 200)
    check_to_accept_terms_and_condition = forms.BooleanField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        client = Client.objects.create(user=user)
        client.home_address=self.cleaned_data.get('home_address')
        client.phone_number=self.cleaned_data.get('phone_number')
        client.middle_name=self.cleaned_data.get('middle_name')
        client.gender=self.cleaned_data.get('gender')
        client.state=self.cleaned_data.get('state')
        client.city=self.cleaned_data.get('city')
        client.lga=self.cleaned_data.get('lga')
        client.language_spoken=self.cleaned_data('language_spoken')
        client.save()
        return user

class FreelancerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True,  widget=forms.TextInput({ "placeholder": "+2348135058802"}), max_length=14 )
    date_of_birth = forms.DateField(required=True, widget = forms.SelectDateWidget(years=range(1920, 2005)))
    nin = forms.CharField(max_length=11)
    skill = forms.CharField()
    city = forms.CharField()
    profile_pic = forms.ImageField(required=True)
    work_address = forms.CharField()
    state = forms.ChoiceField( choices=STATE_CHOICES)
    lga = forms.ChoiceField(choices=LGA_CHOICES)
    gender = forms.ChoiceField( choices=GENDER_CHOICES)
    language_spoken = forms.CharField(max_length =200, widget=forms.TextInput({ "placeholder": "English, Yoruba, Hausa, Ibira,Kogi Fill as many has you can speak"}))
    Trade_Test_Or_License = forms.ImageField(required=False )
    qualification = forms.ChoiceField( choices=QUALIFICATION_CHOICES, required=False )
    referral_Username = forms.CharField(required=False, widget=forms.TextInput({"placeholder":"Cody"}))
    Bank_Name = forms.ChoiceField(choices=BANK_CHOICES)
    Bank_Account_Number = forms.CharField(max_length=10, widget=forms.TextInput({"placeholder":"0009410323"}), required=True)
    check_to_accept_terms_and_condition = forms.BooleanField(required=True)

    def clean_phone_number(self):
            phone_number = self.cleaned_data['phone_number']
            if Freelancer.objects.filter(phone_number=phone_number).exists():
                raise ValidationError(f"{phone_number} already registered")
            return phone_number
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_freelancer = True
        # user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        freelancer = Freelancer.objects.create(user=user)
        freelancer.middle_name=self.cleaned_data.get('middle_name')
        freelancer.date_of_birth=self.cleaned_data.get('date_of_birth')
        freelancer.nin=self.cleaned_data.get('nin')
        freelancer.skill=self.cleaned_data.get('skill')
        freelancer.work_address=self.cleaned_data.get('work_address')
        freelancer.state=self.cleaned_data.get('state')
        freelancer.city=self.cleaned_data.get('city')
        freelancer.lga=self.cleaned_data.get('lga')
        freelancer.profile_pic=self.cleaned_data.get('profile_pic')
        freelancer.gender=self.cleaned_data.get('gender')
        freelancer.phone_number = self.cleaned_data.get('phone_number')
        freelancer.Trade_Test_or_License=self.cleaned_data.get('Trade_Test_or_License')
        freelancer.qualification=self.cleaned_data.get('qualification')
        freelancer.language_spoken=self.cleaned_data.get('language_spoken')
        freelancer.Referral_Username = self.cleaned_data.get('Referral_Username')
        freelancer.Bank_Name = self.cleaned_data.get('Bank_Name')
        freelancer.Bank_Account_Number = self.cleaned_data.get('Bank_Account_Number')
        freelancer.save()
        return user


# class UserLoginForm(forms.Form):
#     email = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))