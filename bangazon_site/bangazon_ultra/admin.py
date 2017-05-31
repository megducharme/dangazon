from django.contrib import admin

# Register your models here.
from bangazon_ultra.models import *
admin.site.register(customer_model.Customer)
admin.site.register(order_model.Order)
admin.site.register(products_model.Product)
admin.site.register(product_types_model.ProductTypes)
admin.site.register(paymenttype_model.PaymentType)