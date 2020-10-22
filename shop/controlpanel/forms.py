from django import forms
from django.db import models
from catalog.models import Category, Product
from orders.models import Order


class CategoryChangeForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'number', 'slug', 'image']


class ProductChangeForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug',
                  'mainimage', 'description', 'code', 'size',
                  'contents', 'price', 'available']


class OrderChangeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone', 'fullname', 'email', 'city',
                  'street', 'house_no', 'flat_no', 'building_no',
                  'postal_code', 'comment', 'call_me', 'paid', 'client_exists']
