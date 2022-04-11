# Generated by Django 3.2.12 on 2022-02-24 18:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Plan title')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('target', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('has_parent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='business.employee')),
            ],
        ),
        migrations.CreateModel(
            name='VisitAgenda',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('APPROVED', 'APPROVED'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'), ('ONGOING', 'ONGOING'), ('CLOSED', 'CLOSED')], default='NEW', max_length=255)),
                ('type', models.CharField(choices=[('SINGLE', 'SINGLE'), ('DOUBLE', 'DOUBLE'), ('COACHED', 'COACHED')], default='SINGLE', max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='business.businessclient')),
            ],
        ),
        migrations.CreateModel(
            name='VisitDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('UPCOMING', 'UPCOMING'), ('IN-PROGRESS', 'IN-PROGRESS'), ('CLOSED', 'CLOSED'), ('MISSED', 'MISSED')], default='UPCOMING', max_length=255)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubPlan',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='plan.plan')),
                ('parent_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='plan.plan')),
            ],
        ),
        migrations.CreateModel(
            name='VisitProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('feedback', models.CharField(default=0, max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='inventory.product')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='plan.visitagenda')),
            ],
        ),
        migrations.CreateModel(
            name='PlanRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='plan.plan')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='business.request')),
            ],
        ),
        migrations.CreateModel(
            name='DoubleVisit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('DOUBLE', 'DOUBLE'), ('COACHED', 'COACHED')], default='SINGLE', max_length=255)),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='visit', to='business.request')),
                ('visit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='plan.visitagenda')),
            ],
        ),
        migrations.AddField(
            model_name='visitagenda',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='plan.subplan'),
        ),
    ]
