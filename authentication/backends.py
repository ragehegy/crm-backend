from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from business.models import Employee

class EmployeeBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']

        try:
            employee = Employee.objects.get(email=email)
            if employee.check_password(password) is True:
                return employee
        except Employee.DoesNotExist:
            pass