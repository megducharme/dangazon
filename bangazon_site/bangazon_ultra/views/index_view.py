from django.shortcuts import get_object_or_404, render
from bangazon_ultra.models import *

def index(request):
    """
    The index view maps the url index.html to the data that it needs.

    Arguments: request allows Django to see user session data
    Author: Zoe, Main Bananas
    """
    most_recent_products = products_model.Product.objects.all().order_by('date_created')[:20]
    # for p_type in producttypes:
    #     p = product_types_model.ProductTypes.objects.get(id=p_type.id).product_set.all().order_by('-id')[:5]
    #     products.extend(p.values())

    return render(request, 'bangazon_ultra/index.html', {'products': most_recent_products})
