# Generated by Django 3.2.5 on 2021-12-26 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('en_name', models.CharField(max_length=255)),
                ('ar_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ClientSpecialty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialties', to='shared.client')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='shared.specialty')),
            ],
        ),
    ]