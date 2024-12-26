
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.cart.cart import Cart
from .models import Product

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    #NOTE The data retrieved from request.POST is always a string.
    product_id = data['product_id']
    update = data['update']#If 'update' is not present, update will be set to None.
    quantity = data['quantity']#If 'quantity' is not present, the default value 1 will be used 
    
    print(data)
    print(data['product_id'])
    cart = Cart(request)
    
    product = get_object_or_404(Product, pk=product_id)
    
    if not update:
        cart.add(product=product, quantity=1, update_quantity=False )
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True )
        
    return JsonResponse(jsonresponse)
    