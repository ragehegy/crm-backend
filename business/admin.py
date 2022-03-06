from django.contrib import admin

from shared.models import City
from adminsite.admin import CustomModelAdmin, custom_admin
from .forms import DistrictEmployeesForm
from .models import *
from .serializers import DistrictEmployeesSerializer

class EmployeeAdmin(CustomModelAdmin):
    pass

class BusinessClientAdmin(CustomModelAdmin):
    pass

class BusinessAdmin(CustomModelAdmin):
    pass

class UnitAdmin(CustomModelAdmin):
    pass

class UnitHeadAdmin(CustomModelAdmin):
    pass

class RequestAdmin(CustomModelAdmin):
    pass

custom_admin.register(Employee, EmployeeAdmin)
custom_admin.register(BusinessClient, BusinessClientAdmin)
custom_admin.register(Business, BusinessAdmin)
custom_admin.register(Unit, UnitAdmin)
custom_admin.register(UnitHead, UnitHeadAdmin)
custom_admin.register(LeaveRequest, RequestAdmin)

class DistrictEmplyoeeAdmin(CustomModelAdmin):
    form = DistrictEmployeesForm
    list_display = ('district', 'employee',)
    exclude = ('employee', )

    def save_model(self, request, obj, form, change) -> None:
        serializer = DistrictEmployeesSerializer(data=form.data)
        serializer.is_valid()

        return serializer.save()

custom_admin.register(DistrictEmplyoee, DistrictEmplyoeeAdmin)

class DistrictInline(admin.TabularInline):
    model = BusinessDistrict
    
class BusinessCityAdmin(admin.ModelAdmin):
    inlines = [DistrictInline,]

custom_admin.register(City, BusinessCityAdmin)


class BrickInline(admin.TabularInline):
    model = DistrictBrick    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'type', 'phone', 'is_active', 'last_login')
    # exclude = ('id', 'business', 'password', 'last_login', 'is_staff')

@admin.register(BusinessDistrict)
class CityBricksAdmin(admin.ModelAdmin):
    # exclude = ('id', 'business',)
    inlines = [BrickInline,]
    # raw_id_fields = ("city",)

