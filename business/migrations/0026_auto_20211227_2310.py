# Generated by Django 3.2.5 on 2021-12-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0025_auto_20211227_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='request_ptr',
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
