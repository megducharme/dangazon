from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models.customer_model import Customer
from bangazon_ultra.models.order_model import Order

def get_customer_orders(request):
    customer = Customer.objects.get(user=request.user)
    print(customer)
    customer_orders = Order.objects.filter(buyer_id = customer)
    context = {'customer_orders': customer_orders}

    return render(request, 'bangazon_ultra/order_history.html', context)
