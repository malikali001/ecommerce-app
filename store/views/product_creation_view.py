from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.forms import modelformset_factory
from store.forms.product_creation_form import ProductForm
from store.models.product import Product
from store.models.image import Image
from store.forms.image_addition_form import ImageAdditionForm
# Create your views here.


class ProductCreationView(View):
    def get(self, request):
        form = ProductForm()
        image_form = ImageAdditionForm()
        return render(request, 'store/add_product.html', {'form': form, 'image_form':image_form})

    def post(self, request):
        form = ProductForm(request.POST)
        images = request.FILES.getlist('image')
        if form.is_valid():
            product_name = form.cleaned_data.get('product_name')
            product_description = form.cleaned_data.get('product_description')
            price = form.cleaned_data.get('price')
            quantity = form.cleaned_data.get('quantity')
            product = Product.objects.create(product_name=product_name, 
                                             product_description=product_description,
                                             price=price,
                                             quantity=quantity, 
                                             user_id=request.user.id)
            product.save()
            for image in images:
                image_obj = Image.objects.create(image=image,product_id=product.id)
                image_obj.save()
            return HttpResponse('product added')
        return HttpResponse(form.errors)
