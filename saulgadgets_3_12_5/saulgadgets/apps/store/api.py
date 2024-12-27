
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.cart.cart import Cart
from .models import Product
import logging
logger = logging.getLogger('apps.cart')
from apps.core.views import debug_function_name


def api_add_to_cart(request):
    debug_function_name()
    data = json.loads(request.body)
    
    jsonresponse = {'success': True}
    #NOTE The data retrieved from request.POST is always a string.
    product_id = data['product_id']
    update = data['update']#If 'update' is not present, update will be set to None.
    quantity = data['quantity']#If 'quantity' is not present, the default value 1 will be used 
    
    logger.debug("Request method: %s", data) 
    cart = Cart(request)
    logger.debug("Request method: %s", str(cart) )
    product = get_object_or_404(Product, pk=product_id)
    
    if not update:
        cart.add(product=product, quantity=1, update_quantity=False )
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True )
        
    return JsonResponse(jsonresponse)
    