from django.db import models
from uuid import uuid4
import os

from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
from django.utils import timezone

from business.models import Business


class Line(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    created = models.DateTimeField(editable=False, default=timezone.now)

    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.title()    


class Product(models.Model):

    def validate_file_extension(file):
        ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
        valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png']
        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file extension.')

    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    category = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField()
    brochure = models.FileField(upload_to='uploads/inventory/products/', blank=True, validators=[validate_file_extension])
    created = models.DateTimeField(editable=False, default=timezone.now)

    line = models.ForeignKey(Line, on_delete=CASCADE, related_name='products')

    def __str__(self) -> str:
        return self.name.title()