from django.test import TestCase
from bangazon_ultra.models.paymenttype_model import *

class PaymentTypeModelTests(TestCase):
    """
        This class tests all aspects of the PaymentType model, which pertains to the creation of new payment types and getting existing payment types from the database.

        Methods:
            test_payment_type_model - Tests the PaymentType model's ability to create a new instance of payment type to add to the database.

        Author: Steven Holmes (Main Bananas)
    """

    def test_paymenttype_model(self):
        self.payment = PaymentType.objects.create(payment_name='Visa', account_number=1234567890, expiration_date='12-12-01', billing_address='123 Test Way')
        self.db_acct = PaymentType.objects.get(pk=1)
        self.assertEqual(self.payment.id, self.db_acct.id)