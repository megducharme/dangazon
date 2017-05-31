from django.test import TestCase
from django.urls import reverse
from bangazon_ultra.models.paymenttype_model import *
from bangazon_ultra.models.customer_model import *
from bangazon_ultra.models.order_model import *
from bangazon_ultra.models.products_model import *
from bangazon_ultra.views.paymenttype_view import *
from django.contrib.auth.models import User

class CompleteOrderViewsTests(TestCase):
    """
        This class tests aspects of the CompleteOrder view methods in relation to the customer's ability to complete a given order. 

        Methods:
            test_user_can_select_payment_type_for_order - Tests user's ability to add a new payment type to be associated with their account and to use for order completion.
            test_user_can_confirm_order_completion - Tests user's ability to view existing payment types upon request. The application should return their payment types from the database and display them to the customer user. 

        Author: Steven Holmes (Main Bananas)
    """
    def setUp(self):
    # Setting up a user & customer, logging user in, creating payment type for testing purposes.
        self.user = User.objects.create_user(
                username = 'test_user',
                password = 'password',
                first_name = 'Testy',
                last_name = 'Testerson',
                email = 'testy@test.com'
                )

        self.customer = Customer.objects.create(
                user = self.user,
                phone = "123-456-7890", 
                shipping_address="123 Testing Way"
                )

        self.payment = PaymentType.objects.create(
                account_number = 1234567890, 
                payment_name = 'Visa', 
                expiration_date = '12-12-17', 
                billing_address = '123 Test Way', 
                customer = self.customer
                )

        PaymentType.objects.create(
                account_number = 1122334455, 
                payment_name = 'AmEx', 
                expiration_date = '01-01-18', 
                billing_address = '12456 Testing Drive', 
                customer = self.customer
                )

        product_type = ProductTypes.objects.create(category_name="Testing")
        self.product = Product.objects.create(
            title="Robot",
            description="Yahoo for robots",
            seller=self.customer,
            product_type=product_type,
            price=9.85,
            quantity=9
        )


        self.client.login(username = 'test_user', password = 'password')

    def test_complete_order_view(self):
        """
        Test that the user can access view for completing order
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)


    def test_user_can_select_payment_type_for_order(self):
        available_payment_types = PaymentType.objects.filter(customer_id = 1)
        chosen_payment_type = available_payment_types[1]
        self.assertEqual(chosen_payment_type.account_number, 1122334455)