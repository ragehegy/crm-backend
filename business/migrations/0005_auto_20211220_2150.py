# Generated by Django 3.2.5 on 2021-12-20 21:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20211220_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessunit',
            name='business',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.business'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9a729adc-7b97-47da-9958-9a2c3e13cc6f'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessdistrict',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f1dd61c8-04b5-48b5-a418-6a347bf63c88'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessunit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('56b2cd48-c691-47ca-9358-52aa23413e3c'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='salesteam',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5f6fc6c2-dc3f-47a6-bdf2-6abcedbd44f5'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f3a31940-e68a-4a67-88fe-931d5701baf2'), primary_key=True, serialize=False, unique=True),
        ),
    ]