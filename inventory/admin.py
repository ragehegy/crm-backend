from django.contrib import admin

from .models import Line, Product

class CustomAdmin(admin.AdminSite):
    login_template = 'admin/login.html'
    
    def login(self, request, extra_context=None):
        print(request.GET)
        print(request.POST)
        return super().login(request, extra_context)


class LineAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

custom_admin = CustomAdmin()

custom_admin.register(Line, LineAdmin)
custom_admin.register(Product, ProductAdmin)