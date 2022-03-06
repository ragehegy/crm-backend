from adminsite.admin import CustomModelAdmin, custom_admin
from .models import Line, Product

class LineAdmin(CustomModelAdmin):
    pass

class ProductAdmin(CustomModelAdmin):
    pass

custom_admin.register(Line, LineAdmin)
custom_admin.register(Product, ProductAdmin)