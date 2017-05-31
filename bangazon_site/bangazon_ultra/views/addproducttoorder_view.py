from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models import *
from django.contrib import messages

def add_product_to_order(request):
    """This method gets data from the product detail page about the product, gets the customer order, and adds product to the order. Then it redirects to products type page"""
    data = request.POST
    print(data)
    product = products_model.Product.objects.get(pk=data['product_id'])
    customer = customer_model.Customer.objects.get(user=request.user)
    order = order_model.Order.objects.get_or_create(buyer = customer, payment_complete=0)
    if product.quantity > 0:
        product.quantity = product.quantity -1
        products_model.Product.objects.filter(pk=product.pk).update(quantity=product.quantity)
        order_model.Product_On_Order.objects.create(
        order=order[0],
        product = product   
        )

    return HttpResponseRedirect(redirect_to='/order')
