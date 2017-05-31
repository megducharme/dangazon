from bangazon_ultra.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def navigation(context):
    """
    The navigation context processor generates the dynamic navbar for the index.html template while passing how many products the active customer has.

    Arguments: This class needs context to know which user is currently active.
    Author:    Nate Baker & Zoe, Main Bananas
    """
    if context.user.is_authenticated():
            # return number of their active products
            customer = customer_model.Customer.objects.get(user=context.user)
            order = order_model.Order.objects.get_or_create(buyer=customer, payment_complete=0)
            order_number = order[0]
            products = order_number.products.all().count()
            welcome_message = 'Welcome '+customer.user.first_name + ' ' + customer.user.last_name
            list_of_nav = [
                {
                    'name':'Product Types',
                    'link': '/productTypes/',
                    'prop': 'left'
                },
                {
                    'name':'Sell Product',
                    'link': '/add/',
                    'prop': 'left'
                },
                {
                    'name': 'View Cart',
                    'link': '/order/',
                    'number': products,
                    'prop': 'right'
                },
                {
                    'name':'Logout',
                    'link': '/logout/',
                    'prop': 'right'
                },
                {
                    'name': welcome_message,
                    'link': '/userProfile/',
                    'prop': 'right'
                }
            ]
            return {'navigation': list_of_nav, 'customer': customer}


    else:
        # if user is not logged in show 0 next to cart
        list_of_nav = [
                {
                    'name':'View Products',
                    'link': '/productTypes/'
                },
                {
                    'name':'Login',
                    'link': '/login/'
                }
            ]
        return {'navigation': list_of_nav}
