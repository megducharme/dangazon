from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models.paymenttype_model import PaymentType
from bangazon_ultra.models.customer_model import Customer
from bangazon_ultra.models.order_model import Order



def checkout(request):
    """
    The checkout method serves data to the checkout template.

    The customer will be returned payment methods associated with their account so that they can complete an order.

    Author: Steven Holmes
    """
    customer = Customer.objects.get(user=request.user)
    payment_types = PaymentType.objects.filter(customer_id = customer)
    context = {'payment_types': payment_types}

    return render(request, 'bangazon_ultra/checkout.html', context)

def confirm_order(request):
    """
    The confirm_order method updates the current order data to associate a payment method with it and mark it's payment as complete.

    Author: Steven Holmes
    """
    data = request.POST
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.get(buyer_id = customer, payment_complete=0)
    order.payment_complete = 1
    order.payment_type_id = data['payment_type_id']
    order.save()
    return HttpResponseRedirect('/')