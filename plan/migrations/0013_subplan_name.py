# Generated by Django 3.2.5 on 2022-03-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0012_alter_subplan_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='name',
            field=models.CharField(default='New subplan', max_length=255, verbose_name='Subplan title'),
        ),
    ]
