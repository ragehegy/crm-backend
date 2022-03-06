from django.contrib.auth.models import Permission, Group

from adminsite.admin import CustomModelAdmin, custom_admin
from .models import User

class UserAdmin(CustomModelAdmin):
    pass

class GroupAdmin(CustomModelAdmin):
    pass

class PermissionAdmin(CustomModelAdmin):
    pass

custom_admin.register(User, UserAdmin)
custom_admin.register(Permission, PermissionAdmin)
custom_admin.register(Group, GroupAdmin)
