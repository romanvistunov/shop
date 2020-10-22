from django import forms
from catalog.models import Product
from cart.cart import Cart

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
    size = forms.CharField(required=True, initial=False,
                           widget=forms.HiddenInput)
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
