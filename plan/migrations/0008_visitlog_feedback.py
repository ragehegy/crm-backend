# Generated by Django 3.2.5 on 2022-03-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0007_visitlog_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitlog',
            name='feedback',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
