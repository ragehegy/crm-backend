from uuid import uuid4

from django.db import models
from django.utils import timezone

PLAN_STATUS = (
    ('NEW', 'NEW'),
    ('APPROVED', 'APPROVED'),
    ('PENDING', 'PENDING'),
    ('REJECTED', 'REJECTED'),
    ('ONGOING', 'ONGOING'),
    ('CLOSED', 'CLOSED'),
)

VISIT_STATUS = (
    ('CREATED', 'CREATED'),
    ('UPCOMING', 'UPCOMING'),
    ('IN-PROGRESS', 'IN-PROGRESS'),
    ('CLOSED', 'CLOSED'),
    ('MISSED', 'MISSED'),
)

class Plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    name = models.CharField('Plan title', blank=False, unique=True, max_length=255)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    target = models.IntegerField(blank=False)
    description = models.TextField(blank=True)
    has_parent = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    employee = models.ForeignKey('business.Employee', on_delete=models.CASCADE, related_name='plans')

    def __str__(self) -> str:
        return '%s (%s - %s)' %(self.name, self.start_date, self.end_date)


class SubPlan(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    name = models.CharField('Subplan title', blank=False, max_length=255, default='New subplan')
    start_date = models.DateField(blank=False, default=timezone.now)
    end_date = models.DateField(blank=False, default=timezone.now)

    employee = models.ForeignKey('business.Employee', on_delete=models.CASCADE, related_name='subplans')
    parent_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='childs')

    def __str__(self) -> str:
        return '%s - %s' %(self.name, self.id)


class PlanRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='requests')
    request = models.ForeignKey('business.Request', on_delete=models.CASCADE, related_name='plan')


class VisitAgenda(models.Model):
    VISIT_TYPES = (
        ('SINGLE', 'SINGLE'),
        ('DOUBLE', 'DOUBLE'),
        ('COACHED', 'COACHED'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    status = models.CharField('Visit History', max_length=255, blank=False, default='UPCOMING', choices=VISIT_STATUS)
    approval_status = models.CharField('Visit Approval Status', max_length=255, blank=False, default='NEW', choices=PLAN_STATUS)
    type = models.CharField(max_length=255, blank=False, default='SINGLE', choices=VISIT_TYPES)
    datetime = models.DateTimeField('Date & Time of Visit', editable=False, default=timezone.now)
    notes = models.CharField(max_length=255, blank=True, default='')
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(editable=False, default=timezone.now)

    plan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, related_name='visits')
    client = models.ForeignKey('business.BusinessClient', on_delete=models.CASCADE, related_name='visits')

    def __str__(self) -> str:
        return '%s - %s' %(self.plan, self.client.client.name)

class VisitLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    status = models.CharField('Visit last entry status', max_length=255, blank=False, default='UPCOMING', choices=VISIT_STATUS)
    activity = models.CharField('Track visit activity', max_length=255, blank=False, default='updated')
    timestamp = models.DateTimeField(editable=False, default=timezone.now)
    feedback = models.IntegerField(blank=False, default=0)

    visit = models.ForeignKey(VisitAgenda, on_delete=models.CASCADE, related_name='logs')

    class Meta:
        ordering = ['-timestamp',]

    def __str__(self) -> str:
        return '%s - %s on %s' %(self.visit, self.status, self.timestamp)

class DoubleVisit(models.Model):
    VISIT_TYPES = (
        ('DOUBLE', 'DOUBLE'),
        ('COACHED', 'COACHED'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    type = models.CharField(max_length=255, blank=False, default='SINGLE', choices=VISIT_TYPES)
    
    visit = models.OneToOneField(VisitAgenda, on_delete=models.CASCADE, related_name='coach')
    request = models.OneToOneField('business.Request', on_delete=models.CASCADE, related_name='visit')

class VisitProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    feedback = models.CharField(max_length=255, blank=False, default=0)
    notes = models.TextField(blank=True)
    
    visit = models.ForeignKey(VisitAgenda, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey('inventory.product', on_delete=models.CASCADE, related_name='visits')

    def __str__(self) -> str:
        return 'visit %s - %s' %(self.visit.id, self.product.name)