from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

from django.contrib import admin
from django.contrib.auth.models import AnonymousUser

from business.models import Employee

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class CustomAdmin(admin.AdminSite):
    login_template = 'admin/login.html'
    
    def login(self, request, extra_context=None):
        business_id = request.POST.get('business_id', None)
        print(request.POST)
        if business_id:
            business = Employee.objects.filter(business_id=business_id, email=request.POST.get('username')).first()
            print("business: ", business)
            if not business:
                return AnonymousUser()
        return super().login(request, extra_context)

custom_admin = CustomAdmin()