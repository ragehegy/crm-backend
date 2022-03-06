from django.contrib import admin
from adminsite.admin import custom_admin, CustomModelAdmin

from .models import City, Client, Governorate

class GovernCitiesTab(admin.TabularInline):
    model = City

class BusinessCityAdmin(CustomModelAdmin):
    # exclude = ('id', 'business',)
    inlines = [GovernCitiesTab,]


class ClientAdmin(CustomModelAdmin):
    pass

custom_admin.register(Client, ClientAdmin)

custom_admin.register(Governorate, BusinessCityAdmin)