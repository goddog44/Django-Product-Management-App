from django import forms
from .models import *

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(max_digits=8, decimal_places=2)
#     quantity = forms.IntegerField()

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name','price]
        # excludes = ['name','pricer',]
        