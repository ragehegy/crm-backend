from django.contrib import admin

from .models import Line, Product

from adminsite.admin import CustomModelAdmin, custom_admin, CustomAdmin
from utils.resolve_host import get_tenant

class LineAdmin(CustomModelAdmin):

    def get_queryset(self, request):
        print(get_tenant(request))
        return super().get_queryset(request)

class ProductAdmin(CustomModelAdmin):
    pass

custom_admin.register(Line, LineAdmin)
custom_admin.register(Product, ProductAdmin)