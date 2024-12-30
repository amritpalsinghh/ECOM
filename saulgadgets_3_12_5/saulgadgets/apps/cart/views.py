from django.shortcuts import render
from .cart import Cart
from apps.core.views import debug_function_name
import logging
import json
logger = logging.getLogger('apps.cart')
# Create your views here.
def cart_detail(request):
    debug_function_name()
    cart = Cart(request)
    productsstring =''
    #for item in cart:
     #    print("FORLOOP = "+ str(item))
    for item in cart:
        product = item['product']
        print(item)
        b = "{\"id\":"+str(product.id)+",\"title\":\""+product.title+"\",\"price\":"+str(product.price)+",\"quantity\":"+str(item['quantity'])+"},"
        productsstring = productsstring + str(b)
        
        #productsstring='[{"id": 1, "title": "Laptop", "price": 100, "quantity": 2}, {"id": 2, "title": "Mouse", "price": 50, "quantity": 1}]'
#                 
    print("xxxxxxx")
    productsstring=productsstring.rstrip(',')
    productsstring=f'[{productsstring}]'
    print(productsstring) 
    context = {
        'cart' : cart,
        'productsstring': productsstring  # Serialize as JSON
    }
    return render(request, 'cart_detail.html',context)