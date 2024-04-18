from django.shortcuts import render
from .models import Products
# Create your views here.


def products(request):
    products = Products.objects.all().order_by("-id")
    context = { "products" : products }
    return render(request, "products/products.html", context)