from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from store.models.product import Product
from store.forms.image_addition_form import ImageAdditionForm


class ProductUpdate(UpdateView):
    model = Product
    fields = ["product_name", "product_description", "price", "quantity"]
    template_name = 'store/product_update.html'
    success_url = reverse_lazy("list-product")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image"] = ImageAdditionForm()
        return context