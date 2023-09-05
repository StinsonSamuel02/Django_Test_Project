from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

from .models import Product, Clasification
from .serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def products_list(request):
    if request.GET:

        if 'product_name' in request.GET and request.GET['product_name']:
            query = request.GET['product_name']
            products = Product.objects.filter(name__contains=query)
            return render(request, '../templates/products_list.html', {'products': products})
        else:
            return render(request, '../templates/404.html')
    else:
        products = Product.objects.all()
        return render(request, '../templates/products_list.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, '../templates/product_details.html', {'product': product})


def product_new(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        classification_id = request.POST['classification']

        classification = Clasification.objects.get(id=classification_id)

        product = Product(name=name, price=price, description=description, clasification=classification)
        product.save()

        return redirect('products_list')  # Redirecciona a una vista o URL después de crear el producto

    classifications = Clasification.objects.all()
    context = {
        'classifications': classifications
    }

    return render(request, 'product_new.html', context)
