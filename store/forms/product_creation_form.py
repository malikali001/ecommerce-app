from store.models.product import Product
from django import forms



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'price', 'quantity']
        