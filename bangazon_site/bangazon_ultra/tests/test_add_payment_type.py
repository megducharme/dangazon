from django.test import TestCase
from bangazon_ultra.models.paymenttype_model import *
from bangazon_ultra.models.customer_model import *
from bangazon_ultra.views.paymenttype_view import *
from django.contrib.auth.models import User

class PaymentTypeViewTest(TestCase):
    """
        This class tests all aspects of PaymentTypes in relation to the customer, the database, and interactions with the Bangazon ultra interface. 

        Methods:
            test_paymenttype_view - Tests that the payment type view returns the expected http response. 
            test_user_can_add_new_payment_type - Tests user's ability to add a new payment type to be associated with their account and to use for order completion.
            test_user_can_view_existing_payment_types - Tests user's ability to view existing payment types upon request. The application should return their payment types from the database and display them to the customer user. 

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
                shipping_address="123 Testing Way", 
                )

        self.client.login(username = 'test_user', password = 'password')


    def test_paymenttype_view(self):
        """
            Test that payment type view returns correct http response
        """

        resp = self.client.get('/payment/')
        self.assertEqual(resp.status_code, 200)
        

    def test_user_can_add_new_payment_type(self):
        """
            Test user can add new payment type to associate with their account
        """

        self.payment = PaymentType.objects.create(
                account_number = 1234567890, 
                payment_name = 'Visa', 
                expiration_date = '12-12-17', 
                billing_address = '123 Test Way', 
                customer = self.customer
                )

        self.saved_payment = PaymentType.objects.get(id = 1)
        self.assertEqual(self.saved_payment.pk, self.payment.pk)


    def test_user_can_view_existing_payment_types(self):
        """
            Test user can request and be returned all payment types associated with their account
        """

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
        
        existing_payment_types = PaymentType.objects.filter(customer_id = 1)
        for item in existing_payment_types:
            if item.customer_id == 1:
                self.assertEqual(item.customer_id, self.user.id)


