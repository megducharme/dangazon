from django.test import TestCase
from bangazon_ultra.models.products_model import *
from bangazon_ultra.models.product_types_model import *
from bangazon_ultra.models.customer_model import *
from django.contrib.auth.models import User
# Run `python manage.py test bangazon_ultra`
# from the root directory to run all tests

class ProductsModelTestCase(TestCase):
    """
    The ProductsModelTestCase class tests everything related to testing if products can be added to the database.

    Arguments: TestCase identifies the classes as a test class.
    Methods:   test_products_can_be_added_to_database
    Author:    Nate Baker, Main Bananas
    """

    def test_products_can_be_added_to_database(self):
        """
        test_products_can_be_added_to_database is a method to test if products can be added to the database.
        """

        # create user
        Bill = User.objects.create_user(
            username="billy23332",
            last_name ="Billerton",
            )
        # inject user into customer
        self.Bill = Customer.objects.create(
            user=Bill,
            phone = "333-333-4444",
            shipping_address="123 Bill Way",
            # date_account_created="2017-02-22",
            )

        # pull instance of customer from databse
        bill_in_datebase = Customer.objects.get(user=Bill)
        # check that what is pushed up is what is in the database
        self.assertEqual(bill_in_datebase.pk, Bill.pk)

        # create new product type
        Food = ProductTypes.objects.create(category_name="food")
        # pull instance of product type from databse
        food_in_datebase = ProductTypes.objects.get(category_name="food")
        # check that what is pushed up is what is in the database
        self.assertEqual(food_in_datebase.pk, Food.pk)

        # create new product
        Pizza = Product.objects.create(
            title="Cheese Pizza",
            description="This is a super cheesy pizza.",
            seller=self.Bill,
            product_type=Food,
            price=9.85,
            quantity=9
        )
        # pull instance of product from databse
        pizza_in_datebase = Product.objects.get(title="Cheese Pizza")
        # check that what is pushed up is what is in the database
        self.assertEqual(pizza_in_datebase.pk, Pizza.pk)
