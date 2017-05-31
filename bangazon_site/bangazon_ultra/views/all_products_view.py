from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from bangazon_ultra.models.product_types_model import *
from bangazon_ultra.models.products_model import *

def all_products(request, productTypes_id):
    """
    The all_produdcts views maps the url all_products.html to the data that it needs.

    Arguments: request allows Django to see user session data, and productTypes_id is needed to display the proper product type
    Author: Ike, Main Bananas
    """
    all_products = Product.objects.filter(product_type=productTypes_id)
    product_type_name = ProductTypes.objects.get(id=productTypes_id)
    context =  {'products' : all_products, "productTypes_id": productTypes_id, "product_type_name":product_type_name.category_name}
    return render(request, 'bangazon_ultra/all_products.html', context)