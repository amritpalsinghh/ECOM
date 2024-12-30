from django.conf import settings
from apps.store.models import Product
from apps.core.views import debug_function_name
import logging
logger = logging.getLogger('apps.cart')
class Cart(object):
    def __init__(self,request):
        debug_function_name()
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        print("1")
        print(cart)
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            print("2")
            print(cart)
            
        self.cart = cart
    
    def __iter__(self):
        debug_function_name()
        product_ids = self.cart.keys()
        
        product_clean_ids = []
        for p in product_ids:
            product_clean_ids.append(p)   
            self.cart[str(p)]['product']  = Product.objects.get(pk=p)
            print("rrrrrr")
            print(self.cart)
            
        for item in self.cart.values():
            print("oooooo")
            print(item)
            item['total_price'] = int(item['price'])* int(item['quantity'])
            yield item    
        
            
        def __len__(self):
            
            return sum(item['quantity'] for item in self.cart.values())
                
            
            
    def add(self, product, quantity=1, update_quantity=False ):
        debug_function_name()
        product_id = str(product.id)
        price = product.price

        print('Product_id:', product_id)

        if product_id not in self.cart:
            print("1")
            self.cart[product_id] = {'quantity':1,'price':price,'id': product_id}
            
        if update_quantity:
            print("2")
            self.cart[product_id]['quantity'] = quantity
        else:
            print("3")
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
            
        self.save()
    
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def save(self):
        debug_function_name()
        logger.debug("Request method: %s", "AMRIT")
        print("15")
        print(self.cart)
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True