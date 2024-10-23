from unicodedata import name
from django.urls import path
from store.views import user_creation_view, user_updation_view, user_email_validation_view, product_creation_view
from store.views.product_delete_view import ProductDelete
from store.views.product_detail_view import ProductDetail
from store.views.product_list_view import ProductList
from store.views.product_update_view import ProductUpdate 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('signup/', user_creation_view.UserView.as_view(), name='signup'),
    path('update/', user_updation_view.UserUpdateView.as_view(), name='update'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('email-validate/', user_email_validation_view.EmailConfirmation.as_view(), name='email-validate'),


    path('add-product/', product_creation_view.ProductCreationView.as_view(), name='add-product'),
    path('list-product/', ProductList.as_view(), name='list-product'),
    path('detail-product/<int:pk>/', ProductDetail.as_view(), name='detail-product'),
    path('update-product/<int:pk>/', ProductUpdate.as_view(), name='update-product'),
    path('delete-product/<int:pk>/', ProductDelete.as_view(), name='delete-product'),
]