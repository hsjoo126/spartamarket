from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import ProductsForm
# Create your views here.


def products(request):
    products = Products.objects.all().order_by("-id")
    context = { "products" : products }
    return render(request, "products/products.html", context)

def create(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author =  request.user
            product.save()
            return redirect('products:detail', product.pk)
    else:
        form = ProductsForm()

    context = { "form" : form }
    return render(request, 'products/create.html', context)

def detail(request, pk):
    products = get_object_or_404(Products,pk = pk)
    context = { "products" : products }
    return render(request, "products/detail.html", context)

def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products,pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect("products:products")
    return redirect("accounts:login")

def update(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('products:detail', product.pk)
    else:
        form = ProductsForm(instance=product)
    
    context = { 
        "form" : form ,
        "product" : product
        }
    return render(request, 'products/update.html', context)

def delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=pk)
        product.delete()
        return redirect('products:products')
    return redirect('products:detail', pk)
