from django.contrib import admin
from .models import UOM, Customer, City, Category, Pack, Product, SaleMST, SaleDTL, Vendor, PurchaseMST, PurchaseDTL
# Registering models here.
admin.site.register(Customer)
admin.site.register(UOM)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Pack)
admin.site.register(Product)
admin.site.register(SaleMST)
admin.site.register(SaleDTL)
admin.site.register(Vendor)
admin.site.register(PurchaseMST)
admin.site.register(PurchaseDTL)