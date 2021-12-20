from django.db import models
from uuid import uuid4

from django.db.models.deletion import CASCADE
from django.utils import timezone

from business.models import Business


class Line(models.model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField(blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, default=timezone.now)

    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.title()    


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), unique=True)
    name = models.CharField(blank=False, unique=True)
    category = models.CharField()
    description = models.CharField()
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False, default=timezone.now)

    line = models.ForeignKey(Line, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name.title()