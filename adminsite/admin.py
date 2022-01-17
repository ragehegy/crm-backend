from django.contrib import admin

class CustomAdmin(admin.AdminSite):
    login_template = 'admin/login.html'
    
    def login(self, request, extra_context=None):
        print(request.GET)
        print(request.POST)
        return super().login(request, extra_context)

custom_admin = CustomAdmin()