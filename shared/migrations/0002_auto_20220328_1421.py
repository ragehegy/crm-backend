# Generated by Django 3.2.5 on 2022-03-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_class',
            field=models.CharField(default='B', max_length=5),
        ),
        migrations.AddField(
            model_name='client',
            name='type',
            field=models.CharField(default='AM', max_length=5),
        ),
    ]
