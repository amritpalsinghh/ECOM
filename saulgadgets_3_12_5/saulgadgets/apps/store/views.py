from apps.core.views import debug_function_name
from django.shortcuts import render,get_object_or_404
from apps.store.models import Product , Category
import logging
logger = logging.getLogger('apps.store')
# Create your views here.
# TODO ddfd
# BUG
# def debug_function_name():
#     # Prints the name of the function from which it is called
#     print(f"Entered function: {inspect.currentframe().f_back.f_code.co_name}")
    
def product_detail(request, category_slug, slug):
    debug_function_name()
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
    debug_function_name()
    category = get_object_or_404(Category, slug=slug)
    product= category.products.all()
    
    context = {
        'category': category,
        'product': product
    }
    return render(request, 'category_detail.html', context) 
