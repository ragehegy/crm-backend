# Generated by Django 3.2.5 on 2021-12-26 22:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dff68f55-837a-4bee-b6d1-c7d2c823da5b'), primary_key=True, serialize=False, unique=True),
        ),
    ]
