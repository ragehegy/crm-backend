# Generated by Django 3.2.5 on 2021-12-27 21:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0020_auto_20211227_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.UUIDField(default=uuid.UUID('126de449-cbfd-4564-9dff-e8516572fdfb'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessclient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9b3bd546-2aff-4e0a-a357-44bdb1228ba2'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessdistrict',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2433024c-8285-45df-b737-471a4221ff7c'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='districtemployeeline',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cfb1bcf1-7d9e-4471-9b4e-0369b372c7fe'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='districtemplyoee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1a9ecd7c-860c-42d8-9839-a4713e89a55c'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.UUIDField(default=uuid.UUID('514ef883-9dee-454c-b22e-08995ed55d9f'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='salesteam',
            name='id',
            field=models.UUIDField(default=uuid.UUID('54426715-220c-4345-84d3-a5c63270539a'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.UUIDField(default=uuid.UUID('52defc65-8727-4dd0-833b-69156f78f7be'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f8eaf7a8-bdb4-4c6f-b98e-ee69ebddfa13'), primary_key=True, serialize=False, unique=True),
        ),
    ]
