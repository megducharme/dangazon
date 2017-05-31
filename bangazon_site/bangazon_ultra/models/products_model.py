from django.db import models
from . import customer_model, product_types_model


class Product(models.Model):
    """
    The ProductModel class creates the product table and all related fields in the database.

    Arguments: The models.Model argument lets Django know this class will be used to create a database table.
    Author:    Nate Baker, Main Bananas
    """
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    seller = models.ForeignKey(customer_model.Customer, blank = True, null=True)
    product_type = models.ForeignKey(product_types_model.ProductTypes, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    product_image = models.FileField()

