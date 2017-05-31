from django.test import TestCase
from bangazon_ultra.models.products_model import *
from bangazon_ultra.models.product_types_model import *
from bangazon_ultra.models.customer_model import *
from bangazon_ultra.views.product_details_view import *
from django.urls import reverse
# Run `python manage.py test bangazon_ultra`
# from the root directory to run all tests

class ProductDetailsTestCase(TestCase):
    """
    The ProductDetailsTestCase class tests everything related to testing if the Product Details View is working.

    Arguments: TestCase identifies the classes as a test class.
    Methods:   test_product_detail_view_shows_product_data
    Author:    Zoe LeBlanc, Main Bananas
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

        product_type = product_types_model.ProductTypes.objects.create(category_name="Test")

        self.product = products_model.Product.objects.create(
            title="Cheese Pizza",
            description="This is a super cheesy pizza.",
            seller=self.customer,
            product_type=product_type,
            price=9.85,
            quantity=9
        )

        self.client.login(
            username = "zoe",
            password = "1234asdf"
        )

    def test_product_detail_view_shows_product_data(self):
        """
        test_product_detail_view_shows_product_data tests if a product can be created and then displayed on a product details view.
        """
        response = self.client.get(reverse('bangazon_ultra:product_detail', args={self.product.pk}))
        self.assertEqual(response.context['product'].pk, self.product.pk)

