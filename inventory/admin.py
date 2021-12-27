from django.contrib import admin

from .models import Line, Product


@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
