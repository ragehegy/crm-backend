# Generated by Django 3.2.5 on 2022-03-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0009_remove_visitlog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitlog',
            name='status',
            field=models.CharField(choices=[('UPCOMING', 'UPCOMING'), ('IN-PROGRESS', 'IN-PROGRESS'), ('CLOSED', 'CLOSED'), ('MISSED', 'MISSED')], default='UPCOMING', max_length=255, verbose_name="Visit last entry's status"),
        ),
    ]
