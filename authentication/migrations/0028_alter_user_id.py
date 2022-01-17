# Generated by Django 3.2.5 on 2021-12-27 21:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('838ddf38-9b07-4d14-ad24-89dde16059cd'), primary_key=True, serialize=False, unique=True),
        ),
    ]