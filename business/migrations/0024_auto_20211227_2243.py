# Generated by Django 3.2.5 on 2021-12-27 22:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0023_auto_20211227_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaverequest',
            old_name='type',
            new_name='leave_type',
        ),
        migrations.AddField(
            model_name='request',
            name='type',
            field=models.CharField(choices=[('LEAVE', 'LEAVE'), ('COACHED_VISIT', 'COACHED_VISIT'), ('PLAN', 'PLAN')], default='LEAVE', max_length=255),
        ),
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.UUIDField(default=uuid.UUID('42aae5ae-c00a-4551-9103-a8702ba4e40e'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessclient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('31bca1e7-a7bd-4d51-936e-9e75e1dfef6c'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessdistrict',
            name='id',
            field=models.UUIDField(default=uuid.UUID('01ba00a4-0528-4275-9d07-2428c843b30e'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='districtemployeeline',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d824ce92-9d94-45f1-8bd1-0ab1a5e31134'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='districtemplyoee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('61ed875d-2cc5-4a21-b269-0dedb58c667d'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.UUIDField(default=uuid.UUID('52473630-a043-4ca7-a7d5-bdea1eae951e'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='salesteam',
            name='id',
            field=models.UUIDField(default=uuid.UUID('aff9bf0b-71d8-4381-8f93-a7e90ac4214b'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.UUIDField(default=uuid.UUID('15592bb4-050e-4192-b01a-062d26693490'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('66c32cf2-614a-4965-a98f-24a22238aa9b'), primary_key=True, serialize=False, unique=True),
        ),
    ]