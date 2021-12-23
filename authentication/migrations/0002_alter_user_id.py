# Generated by Django 3.2.5 on 2021-12-17 22:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2678b3c2-09de-4ab0-8f9a-9c4a61678d78'), primary_key=True, serialize=False, unique=True),
        ),
    ]