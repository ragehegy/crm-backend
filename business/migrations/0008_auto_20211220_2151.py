# Generated by Django 3.2.5 on 2021-12-20 21:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_auto_20211220_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.UUIDField(default=uuid.UUID('61b60838-db79-493b-8243-e851e9dfc345'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='businessdistrict',
            name='id',
            field=models.UUIDField(default=uuid.UUID('12e1c199-30d5-4153-9b64-4fdb6fa94faa'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='salesteam',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7d3e3aee-7115-4858-9edc-12b4f74e9443'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5a5a10ba-a1ee-4468-9cb0-4cb7f9d80637'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.RenameModel(
            old_name='BusinessUnitHead',
            new_name='UnitHead',
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('e7f591dd-30c5-4975-87bc-15247d2860ef'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Unit name')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
            ],
        ),
        migrations.AlterField(
            model_name='salesteam',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.unit'),
        ),
        migrations.AlterField(
            model_name='unithead',
            name='unit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.unit'),
        ),
        migrations.DeleteModel(
            name='BusinessUnit',
        ),
    ]
