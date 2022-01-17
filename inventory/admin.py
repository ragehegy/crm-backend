from django.contrib import admin

from .models import Line, Product

from adminsite.admin import custom_admin

class LineAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

custom_admin.register(Line, LineAdmin)
custom_admin.register(Product, ProductAdmin)