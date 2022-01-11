from django.contrib import admin

from .models import City, Client, Governorate

class GovernCitiesTab(admin.TabularInline):
    model = City

@admin.register(Governorate)
class BusinessCityAdmin(admin.ModelAdmin):
    # exclude = ('id', 'business',)
    inlines = [GovernCitiesTab,]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass