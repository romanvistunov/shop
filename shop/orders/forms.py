from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'fullname', 'email', 'city',
        'street', 'house_no', 'flat_no', 'building_no',
        'postal_code', 'comment', 'call_me',]

