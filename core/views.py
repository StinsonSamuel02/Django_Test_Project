from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from api.models import Product


# Create your views here.
def dashboard(request):
    return render(request, "base.html")


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, '../templates/product_details.html', {'product': product})
