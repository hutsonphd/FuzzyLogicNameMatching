# Generated by Django 4.0.4 on 2022-04-28 00:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entso',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entso_unit_id', models.CharField(default=None, max_length=1024, null=True)),
                ('unit_capacity', models.CharField(default=None, max_length=1024, null=True)),
                ('unit_fuel', models.CharField(default=None, max_length=1024, null=True)),
                ('country', models.CharField(default=None, max_length=1024, null=True)),
                ('unit_name', models.CharField(default=None, max_length=1024, null=True)),
                ('plant_name', models.CharField(default=None, max_length=1024, null=True)),
                ('plant_capacity', models.CharField(default=None, max_length=1024, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Entso',
                'db_table': 'entso',
                'ordering': ['plant_name'],
            },
        ),
        migrations.CreateModel(
            name='Gppd',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gppd_plant_id', models.CharField(default=None, max_length=1024, null=True)),
                ('plant_name', models.CharField(default=None, max_length=1024, null=True)),
                ('latitude', models.CharField(default=None, max_length=1024, null=True)),
                ('longitude', models.CharField(default=None, max_length=1024, null=True)),
                ('platts_plant_id', models.CharField(default=None, max_length=1024, null=True)),
                ('country', models.CharField(default=None, max_length=1024, null=True)),
                ('country_long', models.CharField(default=None, max_length=1024, null=True)),
                ('plant_capacity', models.CharField(default=None, max_length=1024, null=True)),
                ('plant_primary_fuel', models.CharField(default=None, max_length=1024, null=True)),
                ('commissioning_year', models.CharField(default=None, max_length=1024, null=True)),
                ('owner', models.CharField(default=None, max_length=1024, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Gppd',
                'db_table': 'gppd',
                'ordering': ['plant_name'],
            },
        ),
        migrations.CreateModel(
            name='Platts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('platts_plant_id', models.CharField(default=None, max_length=1024, null=True)),
                ('platts_unit_id', models.CharField(default=None, max_length=1024, null=True)),
                ('plant_name', models.CharField(default=None, max_length=1024, null=True)),
                ('unit_name', models.CharField(default=None, max_length=1024, null=True)),
                ('owner', models.CharField(default=None, max_length=1024, null=True)),
                ('unit_capacity', models.CharField(default=None, max_length=1024, null=True)),
                ('year_commissioned', models.CharField(default=None, max_length=1024, null=True)),
                ('unit_fuel', models.CharField(default=None, max_length=1024, null=True)),
                ('city', models.CharField(default=None, max_length=1024, null=True)),
                ('state', models.CharField(default=None, max_length=1024, null=True)),
                ('region', models.CharField(default=None, max_length=1024, null=True)),
                ('country', models.CharField(default=None, max_length=1024, null=True)),
                ('subregion', models.CharField(default=None, max_length=1024, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Platts',
                'db_table': 'platts',
                'ordering': ['plant_name'],
            },
        ),
    ]
