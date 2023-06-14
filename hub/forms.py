from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from django import forms

class ReceiptForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    quantity = forms.IntegerField(label='Quantity', min_value=1)
    price = forms.DecimalField(label='Price', min_value=0.01, max_digits=8, decimal_places=2)

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        price = cleaned_data.get('price')

        if quantity and price:
            total = quantity * price
            cleaned_data['total'] = total

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('price', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('quantity', css_class='form-group col-md-6 mb-0'),
                Column('total', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )
