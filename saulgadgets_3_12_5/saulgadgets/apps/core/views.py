from django.shortcuts import render

from apps.store.models import Product
# Create your views here.
def index(request):
    products = Product.objects.filter(is_featured=True)
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def contact(request): 
    return render(request, 'contact.html')

def about(request): 
    return render(request, 'about.html')
