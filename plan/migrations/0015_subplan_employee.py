# Generated by Django 3.2.5 on 2022-04-06 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20220324_1246'),
        ('plan', '0014_auto_20220329_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='employee',
            field=models.ForeignKey(default='80c390e2-844a-4ded-ad5d-9d2d9026450b', on_delete=django.db.models.deletion.CASCADE, related_name='subplans', to='business.employee'),
            preserve_default=False,
        ),
    ]
