# Generated by Django 3.2.5 on 2021-12-23 20:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_auto_20211221_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cfecd87e-6e02-44bd-937f-d5fa7f3d2a41'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessdistrict',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1ea1be90-05cb-4eba-98aa-4b93d9ab40ef'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='type',
            field=models.CharField(choices=[('UNIT_HEAD', 'UNIT_HEAD'), ('DISTRICT_MANAGER', 'DISTRICT_MANAGER'), ('MEDICAL_REP', 'MEDICAL_REP')], max_length=255),
        ),
        migrations.AlterField(
            model_name='salesteam',
            name='id',
            field=models.UUIDField(default=uuid.UUID('807ddee8-f1e1-4de1-a453-d25294916c0a'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8f6f1e65-3a43-4d2e-93f5-50d174a15978'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1d803c88-d609-4066-99b4-42ce2c947840'), primary_key=True, serialize=False, unique=True),
        ),
    ]
