from uuid import uuid4

from django.db import models
from django.utils import timezone


PLAN_STATUS = (
    ("NEW", "NEW"),
    ("APPROVED", "APPROVED"),
    ("PENDING", "PENDING"),
    ("REJECTED", "REJECTED"),
    ("ONGOING", "ONGOING"),
    ("CLOSED", "CLOSED"),
)

VISIT_STATUS = (
    ("UPCOMING", "UPCOMING"),
    ("IN_PROGRESS", "IN_PROGRESS"),
    ("CLOSED", "CLOSED"),
    ("MISSED", "MISSED"),
)

class Plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField("Plan title", blank=False, unique=True, max_length=255)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    target = models.IntegerField(blank=False)
    description = models.TextField(blank=True)
    has_parent = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    employee = models.ForeignKey('business.Employee', on_delete=models.CASCADE, related_name='plans')

    def __str__(self) -> str:
        return "%s (%s - %s)" %(self.name, self.start_date, self.end_date)


class SubPlan(models.Model):

    id = models.OneToOneField(Plan, primary_key=True, on_delete=models.CASCADE)
    parent_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='childs')


class PlanRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='requests')
    request = models.ForeignKey('business.Request', on_delete=models.CASCADE, related_name='plan')


class VisitAgenda(models.Model):
    VISIT_TYPES = (
        ("SINGLE", "SINGLE"),
        ("DOUBLE", "DOUBLE"),
        ("COACHED", "COACHED"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    status = models.CharField(max_length=255, blank=False, default='NEW', choices=PLAN_STATUS)
    type = models.CharField(max_length=255, blank=False, default='SINGLE', choices=VISIT_TYPES)

    plan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, related_name='visits')
    client = models.ForeignKey('business.BusinessClient', on_delete=models.CASCADE, related_name='visits')


class DoubleVisit(models.Model):
    VISIT_TYPES = (
        ("DOUBLE", "DOUBLE"),
        ("COACHED", "COACHED"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    type = models.CharField(max_length=255, blank=False, default='SINGLE', choices=VISIT_TYPES)
    
    visit = models.OneToOneField(VisitAgenda, on_delete=models.CASCADE, related_name='coach')
    request = models.OneToOneField('business.Request', on_delete=models.CASCADE, related_name='visit')


class VisitDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    status = models.CharField(max_length=255, blank=False, default='UPCOMING', choices=VISIT_STATUS)
    timestamp = models.DateTimeField(editable=False, default=timezone.now)
    notes = models.TextField(blank=True)


class VisitProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    feedback = models.CharField(max_length=255, blank=False, default=0)
    notes = models.TextField(blank=True)
    
    visit = models.ForeignKey(VisitAgenda, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey('inventory.product', on_delete=models.CASCADE, related_name='visits')

    def __str__(self) -> str:
        return "visit %s - %s" %(self.visit.id, self.product.name)