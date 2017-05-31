from django.db import models

class ProductTypes(models.Model):
    """ 
    ProductTypes model class
    The purpose of this class is to define categories of products or product types
    author(s): Ike
    subclasses: Meta (allows forordering by name)
    methods: __str__ : Allows for printing of object in string format
    """
    category_name = models.CharField(max_length=55)

    class Meta:
        ordering = ('category_name',)

        #Allows for the printing of the object in string format
        def __str__(self):
            return '{}'.format(self.category_name)