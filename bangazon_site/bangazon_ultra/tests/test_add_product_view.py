from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from bangazon_ultra.models import *
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AddProductsTest(TestCase):

	def test_user_can_add_products(self):
		
		BillyBob = User.objects.create_user(
					username="BillyBob",
					last_name ="Billerton",
					)
				# inject user into customer
		self.BillyBob = customer_model.Customer.objects.create(
					user=BillyBob,
					phone = "333-333-4444",
					shipping_address="123 Bill Way",
					# date_account_created="2017-02-22",
					)
		food = product_types_model.ProductTypes.objects.get_or_create(category_name="food")

	def test_login_redirects_to_desired_page(self):		
		response = self.client.get(reverse('bangazon_ultra:add'))
		self.assertTemplateUsed('/')
		self.assertEqual(response.status_code, 200)


