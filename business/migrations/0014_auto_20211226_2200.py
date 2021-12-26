# Generated by Django 3.2.5 on 2021-12-26 22:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_clientspecialty_specialty'),
        ('business', '0013_auto_20211226_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.UUIDField(default=uuid.UUID('97090dd5-8153-4485-82b4-c424bc68d32e'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessdistrict',
            name='id',
            field=models.UUIDField(default=uuid.UUID('30df21b1-8413-4578-8042-4d3ac0412076'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='salesteam',
            name='id',
            field=models.UUIDField(default=uuid.UUID('24d58ce9-9d86-4273-a3f1-e34057383ce7'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.UUIDField(default=uuid.UUID('92bf4fed-0a57-4850-baf5-a14cfb9e66d8'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7c91dd70-bd5e-4788-aac2-65c036f16caa'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='BusinessClient',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('9ab12332-8142-46c1-8d62-23c39bb0fb86'), primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='business.business')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='shared.client')),
            ],
        ),
    ]
