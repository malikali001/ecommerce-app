from django.views.generic.list import ListView
from store.models.product import Product



class ProductList(ListView):
    model = Product
    context_object_name = 'data'
    template_name = 'store/product_list.html'