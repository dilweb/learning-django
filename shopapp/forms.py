from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description =  forms.CharField(widget=forms.Textarea, required=False)
    price = forms.DecimalField(max_digits=8, decimal_places=2, initial=0)
    discount = forms.IntegerField(min_value=0, max_value=100, initial=0)
    created_at = forms.DateTimeField(auto_now_add=True)
    archived = forms.BooleanField(required=False, initial=False)