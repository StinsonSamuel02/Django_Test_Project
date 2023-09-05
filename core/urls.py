from django.urls import path
from .views import dashboard, products_list, product_details

app_name = "core"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path(r'products', products_list, name='products_list'),
    path(r'product/<int:product_id>/', product_details, name='product_details'),
]
