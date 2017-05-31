from django.test import TestCase
from bangazon_ultra.models.customer_model import *
from django.contrib.auth.models import User

# Test for successful creation of the model instance. 
# Author: Peter Staggs

class TestCustomerModel(TestCase): 

# First, create an instance of Django's default user object, and specify any of it's default 
# values you want to include in the Customer model: 

	def test_can_create_customer_model(self): 

		Ralph = User.objects.create(
			first_name="Ralph", 
			last_name ="Ralpherson",
			email="r@r.com"
			)
# Next, create the Customer object, with user stored as a value, and test for an instance of it. 

		self.Ralph = Customer.objects.create(
			user= Ralph, 
			phone = "333-333-3333", 
			shipping_address="1234 Cool People Blvd.", 
			)
		
		self.assertIsInstance(self.Ralph, Customer)


