from bangazon_ultra.models import * 
from  django.test import TestCase
from bangazon_ultra.models.product_types_model import ProductTypes

class TestProductTypesModel(TestCase):
    """
    The purpose of this class is to test the model for categories of products on the
    bangazon site.
    Author(s): Ike, Main Bananas
    """

    def test_ProductTypes_model(self):
        """
        The purpose of this function is to test that categories can be added to 
        and retrieved from the database
        Author: Ike, Main Bananas
        """

        #create an instance of a product type ("Shoes")
        shoes = ProductTypes.objects.get_or_create(category_name="Shoes")

        # Test to determine:
        # Does the list of product types equal the 1 product type created
        self.assertEqual( len(ProductTypes.objects.all()), 1 )

    


