from django.contrib import admin

from .models import *

@admin.register(Business)
class Business(admin.ModelAdmin):
    pass


@admin.register(Unit)
class Unit(admin.ModelAdmin):
    exclude = ('id', 'business',)
    


@admin.register(Employee)
class Employee(admin.ModelAdmin):
    exclude = ('id', 'business', 'password', 'last_login', 'is_staff')


@admin.register(UnitHead)
class UnitHead(admin.ModelAdmin):
    pass


@admin.register(BusinessDistrict)
class BusinessDistrict(admin.ModelAdmin):
    exclude = ('id', 'business',)


@admin.register(DistrictEmplyoee)
class DistrictEmplyoee(admin.ModelAdmin):
    pass
