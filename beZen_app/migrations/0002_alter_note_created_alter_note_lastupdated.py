# Generated by Django 4.1.1 on 2022-09-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beZen_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='lastUpdated',
            field=models.DateTimeField(),
        ),
    ]