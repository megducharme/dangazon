from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ultra.models.customer_model import *
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

# This view includes all methods required for creating, authenticating/logging in, and logging
# out a customer.
# Author PS

class CustomerView(TemplateView):
	template_name = "bangazon_ultra/customer_view.html"

class LoginView(TemplateView):
	template_name = "bangazon_ultra/login.html"

class RegisterView(TemplateView):
	template_name = "bangazon_ultra/register.html"

class LogoutView(TemplateView):
	template_name = "bangazon_ultra/logout.html"

class CustomerProfile(TemplateView):
	template_name = "bangazon_ultra/user_profile.html"

# Function for posting user input from the registration form on templates/register.html to the database,
# creating a new User/Customer object and logging them in

def register_customer(request):
	data = request.POST
	user = User.objects.create_user(
		username = data['username'],
		password = data['password'],
		email = data['email'],
		first_name = data['first_name'],
		last_name = data['last_name']
		)
	customer = Customer.objects.create(
		user = user,
		phone = data['phone'],
		shipping_address=data['shipping_address']
		)
	return login_customer(request)

# Logs in returning users based on username and password information

def login_customer(request):
	data = request.POST
	username = data['username']
	password = data['password']
	user = authenticate(
		username = username,
		password = password
		)
	if user is not None:
		login(request = request, user = user)
	else:
# For now, login error redirects head to the index page. This will likely change in future merges.
# Successful login redirects to the productTypes template

		return HttpResponseRedirect(redirect_to='/')
	return HttpResponseRedirect(redirect_to='/productTypes/')

# Logout function will be called via a button on the Navbar
def logout_customer(request):
	logout(request)
	return HttpResponseRedirect(redirect_to='/')
