# Generated by Django 3.2.5 on 2021-12-27 23:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0027_leaverequest_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
