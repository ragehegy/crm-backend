from django.contrib import admin

from adminsite.admin import CustomModelAdmin, custom_admin, CustomAdmin
from business.models import Business
from .models import Line, Product

class LineAdmin(CustomModelAdmin):

    def save_form(self, request, form, change):
        r = super(LineAdmin, self).save_form(request, form, change)
        if not change:
            r.business_id = self.get_business(request).id
        return r
    
    def get_queryset(self, request):
        if self.get_business(request):
            self.exclude = ('id', 'business',)
        return super().get_queryset(request)

class ProductAdmin(CustomModelAdmin):
    pass

custom_admin.register(Line, LineAdmin)
custom_admin.register(Product, ProductAdmin)