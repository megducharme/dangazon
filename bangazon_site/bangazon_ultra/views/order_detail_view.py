from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models import *
from bangazon_ultra.models.order_model import Order, Product_On_Order
from bangazon_ultra.models.products_model import Product

def get_order_details(request, order_id):

    order = Order.objects.filter(id = order_id)
    products_on_order = Product_On_Order.objects.filter(order_id = order_id)
    products = []

    for line_item in products_on_order:
        product = Product.objects.get(id = line_item.product_id)
        products.append(product)
        print(products)

    context = {'order': order, 'products': products}

    return render(request, 'bangazon_ultra/order_detail.html', context)
