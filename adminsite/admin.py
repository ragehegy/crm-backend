from django.contrib import admin
from django.contrib.auth.models import AnonymousUser

from business.models import Employee
from utils.resolve_host import get_business

class CustomAdmin(admin.AdminSite):
    login_template = 'admin/login.html'
    
    def login(self, request, extra_context=None):
        business_id = request.POST.get('business_id', None)
        if business_id:
            business = Employee.objects.filter(business_id=business_id, email=request.POST.get('username')).first()
            if not business:
                return AnonymousUser()
        return super().login(request, extra_context)

custom_admin = CustomAdmin()

class CustomModelAdmin(admin.ModelAdmin):
    def save_form(self, request, form, change):
        r = super().save_form(request, form, change)
        if not change:
            r.business_id = self.get_business(request).id
        return r

    def get_business(self, request):
        return get_business(request)

    def changelist_view(self, request, *args, **kwargs):
        return super().changelist_view(request, *args, **kwargs)

    def get_queryset(self, request):
        if self.get_business(request):
            self.exclude = ('id', 'business',)
        return super().get_queryset(request)