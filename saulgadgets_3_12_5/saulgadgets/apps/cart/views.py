from django.shortcuts import render
from .cart import Cart
from apps.core.views import debug_function_name
# Create your views here.
def cart_detail(request):
    debug_function_name()
    cart = Cart(request)
    print("xxxxxxx")
    #print(cart[0])
    context = {
        'cart' : cart
    }
    return render(request, 'cart_detail.html',context)