# Generated by Django 3.2.5 on 2022-03-25 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_auto_20220325_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitlog',
            name='visit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='plan.visitagenda'),
            preserve_default=False,
        ),
    ]
