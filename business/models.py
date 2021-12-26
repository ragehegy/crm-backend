from uuid import uuid4

from django.db import models
from django.utils import timezone

from authentication.models import User

class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField("Business name", blank=False, unique=True, max_length=255)
    domain = models.CharField("Company preferred domain", blank=False, unique=True, max_length=255)
    address = models.CharField(blank=False, max_length=255)
    phone = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)
    size = models.IntegerField("Company size")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "%s - (%s)" %(self.name, self.domain)


class Employee(User):
    EMPLOYEE_LEVELS = (
        ("UNIT_HEAD", "UNIT_HEAD"),
        ("DISTRICT_MANAGER", "DISTRICT_MANAGER"),
        ("MEDICAL_REP", "MEDICAL_REP"),
    )

    type = models.CharField(max_length=255, choices=EMPLOYEE_LEVELS)

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="employees")
    
    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)


class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField("Unit name", blank=False, unique=True, max_length=255)
    created = models.DateTimeField(editable=False, default=timezone.now)

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="units")

    def __str__(self) -> str:
        return self.name.title()


class UnitHead(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)


class SalesTeam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    title = models.CharField(blank=False, unique=True, max_length=255)
    created = models.DateTimeField(editable=False, default=timezone.now)

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="teams")

    def __str__(self) -> str:
        return self.title.title()


class TeamMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    is_manager = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, default=timezone.now)

    sales_team = models.ForeignKey(SalesTeam, on_delete=models.CASCADE, related_name="members")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="team")


class BusinessDistrict(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField(blank=False, max_length=255)
    created = models.DateTimeField(editable=False, default=timezone.now)
    
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="districts")
    city = models.ForeignKey('shared.City', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.title()


class DistrictEmplyoee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    created = models.DateTimeField(editable=False, default=timezone.now)

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="district")
    district = models.ForeignKey(BusinessDistrict, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.district.name + " " + self.employee.name


class BusinessClient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    created = models.DateTimeField(editable=False, default=timezone.now)
    
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='clients')
    client = models.ForeignKey('shared.Client', on_delete=models.CASCADE, related_name='businesses')


class DistrictEmployeeLine(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    
    employee = models.ForeignKey(DistrictEmplyoee, on_delete=models.CASCADE, related_name='lines')
    line = models.ForeignKey('inventory.Line', on_delete=models.CASCADE, related_name='districts')
    

class Request(models.Model):
    STATUS = (
        ("NEW", "NEW"),
        ("SEEN", "SEEN"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    status = models.CharField(max_length=255, blank=False, default='UPCOMING', choices=STATUS)
    created = models.DateTimeField(editable=False, default=timezone.now)

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='requests')


class LeaveRequest(models.Model):
    id = models.OneToOneField(Request, primary_key=True, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    reason = models.CharField(max_length=255, blank=False)