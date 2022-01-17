# Generated by Django 3.2.5 on 2021-12-27 22:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0011_auto_20211227_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doublevisit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bb54a022-9928-4018-995e-97dd288e8e2d'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d8c2ec2a-b433-4e5b-b301-e8a2c0b6bee0'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='planrequest',
            name='id',
            field=models.UUIDField(default=uuid.UUID('db8c3874-344b-430b-b613-c4093d485e51'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='visitagenda',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fec1e3b3-dad6-4e52-ab21-064899ae5edb'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='visitdetails',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3b6f31b0-a58d-491c-9a1d-48bed7b1fbeb'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='visitproduct',
            name='id',
            field=models.UUIDField(default=uuid.UUID('79ffeb29-1c28-4eef-8163-8bf09d7a5513'), primary_key=True, serialize=False, unique=True),
        ),
    ]