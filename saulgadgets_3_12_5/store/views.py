from django.shortcuts import render,get_object_or_404
from apps.store.models import Product , Category
# Create your views here.
# TODO ddfd
# BUG
def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    
    print(category_slug)
    print(slug)
    print(product.price)
    
    print("amrit")
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def category_detail(request,slug):
    category = get_object_or_404(Category, slug=slug)
    product= category.products.all()
    
    context = {
        'category': category,
        'product': product
    }
    return render(request, 'category_detail.html', context) 
