from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','description']
        widgets={
            'name': forms.TextInput(attrs={'placeholder':'Название товара', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'step':'0.01', 'class':'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':'Описание товара','class':'form-control'})
        }
