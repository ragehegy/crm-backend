from typing import Any
from django.contrib import admin

from .forms import DistrictEmployeesForm
from .models import *
from .serializers import DistrictEmployeesSerializer

from shared.models import City


class DistrictInline(admin.TabularInline):
    model = BusinessDistrict


class BrickInline(admin.TabularInline):
    model = DistrictBrick


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    pass


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    # exclude = ('id', 'business',)
    pass
    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'type', 'phone', 'is_active', 'last_login')
    # exclude = ('id', 'business', 'password', 'last_login', 'is_staff')


@admin.register(UnitHead)
class UnitHeadAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class BusinessCityAdmin(admin.ModelAdmin):
    inlines = [DistrictInline,]


@admin.register(BusinessDistrict)
class CityBricksAdmin(admin.ModelAdmin):
    # exclude = ('id', 'business',)
    inlines = [BrickInline,]
    # raw_id_fields = ("city",)


@admin.register(DistrictEmplyoee)
class DistrictEmplyoeeAdminAdmin(admin.ModelAdmin):
    form = DistrictEmployeesForm
    list_display = ('district', 'employee',)
    exclude = ('employee', )

    def save_model(self, request: Any, obj, form: Any, change: Any) -> None:
        serializer = DistrictEmployeesSerializer(data=form.data)
        serializer.is_valid()

        return serializer.save()


@admin.register(LeaveRequest)
class RequestAdmin(admin.ModelAdmin):
    pass
