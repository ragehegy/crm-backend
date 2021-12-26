from django.db import models
from uuid import uuid4

from django.db.models.deletion import CASCADE
from django.utils import timezone

from business.models import Business


class Line(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    created = models.DateTimeField(editable=False, default=timezone.now)

    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.title()    


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    category = models.CharField(max_length=255, )
    description = models.CharField(max_length=255, )
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(editable=False, default=timezone.now)

    line = models.ForeignKey(Line, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name.title()