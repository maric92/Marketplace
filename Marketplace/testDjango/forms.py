from .models import Company, Product
from django.forms import ModelForm, TextInput


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'name': 'Company'
        })}

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'name': 'Product'
            'decs': 'Description_Product'
        })}

