from django.contrib import admin
from vendors_app import  models


admin.site.register(models.Vendor)
admin.site.register(models.PurchaseOrder)
