from django.shortcuts import render
import inspect
import os
from apps.store.models import Product
# Create your views here.
def debug_function_name():
     # Define ANSI color codes
    YELLOW = "\033[33m"
    ORANGE = "\033[38;5;214m"  # 214 is an approximate orange
    CYAN = "\033[36m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    # Get the current frame and the caller frame
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name  # Function name
    file_name = os.path.basename(frame.f_code.co_filename)  # File name
    
    # Try to retrieve the class name
    cls_name = None
    if 'self' in frame.f_locals:  # For instance methods
        cls_name = frame.f_locals['self'].__class__.__name__
    elif 'cls' in frame.f_locals:  # For class methods
        cls_name = frame.f_locals['cls'].__name__

    # Construct the debug message
    if cls_name:
        message = (
            f"{YELLOW}Entered function: "
            f"{ORANGE}{cls_name}."
            f"{CYAN}{func_name}(){RESET} "
            f"({WHITE}File: {file_name}{RESET})"
        )
    else:
        message = (
            f"{YELLOW}Entered function: "
            f"{CYAN}{func_name}(){RESET} "
            f"({WHITE}File: {file_name}{RESET})"
        )

    # Print the debug message
    print(message)
    
def index(request):
    debug_function_name()
    products = Product.objects.filter(is_featured=True)
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def contact(request): 
    debug_function_name()
    return render(request, 'contact.html')

def about(request): 
    debug_function_name()
    return render(request, 'about.html')
