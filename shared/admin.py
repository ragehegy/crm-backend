from django.contrib import admin

from .models import City, Governorate

class GovernCitiesTab(admin.TabularInline):
    model = City

@admin.register(Governorate)
class BusinessCityAdmin(admin.ModelAdmin):
    # exclude = ('id', 'business',)
    inlines = [GovernCitiesTab,]
