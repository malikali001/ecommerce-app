from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from store.models.product import Product


class ProductDelete(DeleteView):
    model = Product
    context_object_name = "data"
    success_url = reverse_lazy("list-product")
