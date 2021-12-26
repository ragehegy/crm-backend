from uuid import uuid4

from django.db import models


class Governorate(models.Model):
    id = models.AutoField(primary_key=True)
    en_name = models.CharField(blank=False, unique=True, max_length=255)
    ar_name = models.CharField(blank=False, unique=True, max_length=255)

    def __str__(self) -> str:
        return self.en_name.title()


class City(models.Model):
    id = models.AutoField(primary_key=True)
    en_name = models.CharField(blank=False, max_length=255)
    ar_name = models.CharField(blank=False, max_length=255)

    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE, related_name="cities")

    def __str__(self) -> str:
        return self.en_name.title()


class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    en_name = models.CharField(blank=False, max_length=255)
    ar_name = models.CharField(blank=False, max_length=255)

    def __str__(self) -> str:
        return self.en_name


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=255)
    address = models.CharField(blank=False, max_length=255)
    email = models.EmailField(db_index=True, unique=True)    
    phone = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name.title()


class ClientSpecialty(models.Model):
    id = models.AutoField(primary_key=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='specialties')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='clients')

    def __str__(self) -> str:
        return "%s (%s)" %(self.client.name, self.specialty.name)