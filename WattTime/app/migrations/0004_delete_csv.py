# Generated by Django 4.0.4 on 2022-04-28 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_csv_file_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CSV',
        ),
    ]