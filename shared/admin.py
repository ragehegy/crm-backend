from django.contrib import admin
from adminsite.admin import custom_admin

from .models import City, Client, Governorate

class GovernCitiesTab(admin.TabularInline):
    model = City

class BusinessCityAdmin(admin.ModelAdmin):
    # exclude = ('id', 'business',)
    inlines = [GovernCitiesTab,]


class ClientAdmin(admin.ModelAdmin):
    pass

custom_admin.register(Client, ClientAdmin)

custom_admin.register(Governorate, BusinessCityAdmin)