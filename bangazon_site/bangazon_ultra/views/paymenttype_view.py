from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from bangazon_ultra.models.paymenttype_model import PaymentType
from bangazon_ultra.models.customer_model import Customer

def get_payment_types(request):
    customer = Customer.objects.get(user=request.user)
    print(customer)
    payment_types = PaymentType.objects.filter(customer_id = customer)
    context = {'payment_types': payment_types}

    return render(request, 'bangazon_ultra/payment.html', context)

def add_payment_type(request):
    payment = request.POST
    PaymentType.objects.create(
        account_number = payment['account_number'],
        payment_name = payment['payment_name'],
        expiration_date = payment['expiration_date'],
        customer = Customer.objects.get(user=request.user),
        billing_address = payment['billing_address'],
    )

    return HttpResponseRedirect('/')