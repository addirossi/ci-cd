from django.contrib import admin

from .models import Stock, StockProduct, Product

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(StockProduct)
