from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models import *
from bangazon_ultra.models.products_model import *
from django.db.models import F, Sum, Count

def display_order_and_products(request):
    """
    Method to create and display and order and all its products on the order template
    """
    customer = customer_model.Customer.objects.get(user=request.user)
    order = order_model.Order.objects.get_or_create(buyer = customer, payment_complete=0)
    order_item = order[0]
    products = order_item.products.all().values().annotate(Count('id')).order_by('id')
    all_products = products_model.Product.objects.all().order_by('id')
    total =  order_item.products.aggregate(Sum('price'))
    context = {'order': order_item, 'products': products, 'total': total['price__sum'], 'all_products': all_products}
    return render(request, 'bangazon_ultra/order.html', context)
