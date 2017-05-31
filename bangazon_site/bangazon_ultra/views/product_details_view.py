from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models import *


def detail(request, product_id):
    """
    The detail view maps the url product-detail.html to the data that it needs.

    Arguments: request allows Django to see user session data, product_id is used to generate the individual product
    Uncomment the lines to add pictures for each product
    Author: Zoe, Main Bananas
    """

    product = get_object_or_404(products_model.Product, pk=product_id)

    return render(request, 'bangazon_ultra/product_detail.html', {'product': product})

