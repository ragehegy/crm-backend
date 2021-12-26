# Generated by Django 3.2.5 on 2021-12-26 14:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0013_auto_20211226_1457'),
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='parent_plan',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='plan.plan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a2c02d77-6cfa-4114-b9b0-3446913af04f'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='VisitAgenda',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('98f44534-bf06-4a1b-bec9-008c25d8e2ec'), primary_key=True, serialize=False, unique=True)),
                ('rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='business.employee')),
            ],
        ),
    ]
