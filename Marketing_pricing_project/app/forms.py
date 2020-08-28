from django import forms
from .models import ProductTAble

class ProductTableForm(forms.ModelForm):
     prd_id=forms.IntegerField(label='Product ID')
     prd_name=forms.CharField(label='Product NAME')
     prd_qunty=forms.CharField(label='Product Quantity')
     prd_manufdt=forms.DateField(label='Manufacturing Date')
     prd_expdt = forms.DateField(label='Expiry Date')
     prd_price = forms.IntegerField(label='Product Price')
     class Meta:
        model=ProductTAble
        fields="__all__"


