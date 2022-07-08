from django import forms
from categories.models import Product

class ProductEnrollForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput)