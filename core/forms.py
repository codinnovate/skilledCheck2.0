from django import forms
from .models import Payment
from accounts.models import User


class PaymentForm(forms.ModelForm):
   amount = forms.CharField(initial=5500, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
   email = User.email
   class Meta:
        model = Payment
        fields = ('amount', 'email')



# class MyForm(forms.Form):
#     my_field = forms.CharField(initial='default value')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['my_field'].widget.attrs['disabled'] = 'disabled'
