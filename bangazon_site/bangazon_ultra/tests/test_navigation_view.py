from django.test import TestCase
from bangazon_ultra.models import *
from django.urls import reverse
from django.contrib.auth.models import Permission, User


# Run `python manage.py test bangazon_ultra`
# from the root directory to run all tests

class NavigationViewTestCase(TestCase):
    """
    The NavigationViewTestCase class tests everything related to data appearing in the navigation bar

    Arguments: TestCase identifies the classes as a test class.
    Methods:   test_navigation_bar_knows_number_of_products_on_order
    Author:    Nate Baker, Main Bananas
    """

    def setUp(self):
        '''This method sets up initial instances of Customer from the database'''
        user = User.objects.create_user(
            first_name = "Zoe",
            last_name = "LeBlanc",
            username = "zoe",
            email = "z@z.com",
            password = "1234asdf"
        )
        self.customer = customer_model.Customer.objects.create(
            user = user,
            phone = "513498234",
            shipping_address="asdfasf"
        )
        self.client.login(
            username = "zoe",
            password = "1234asdf"
        )

    def test_navigation_bar_knows_number_of_products_on_order(self):
        """
        test_navigation_bar_knows_number_of_products_on_order is a method to test if the the homepage loads. In the future, a better test could be written to make sure the nnavigation bar has a method that returns the number of products on an order for the active user.
        """

        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
