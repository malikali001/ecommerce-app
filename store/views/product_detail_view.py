from django.views.generic.detail import DetailView
from store.models.product import Product
from store.models.image import Image


class ProductDetail(DetailView):
    model = Product
    context_object_name = "data"
    template_name = "store/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = Image.objects.filter(product_id=self.kwargs['pk'])
        return context
