# Generated by Django 3.2.7 on 2021-10-14 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0014_auto_20211014_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservedbook',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 2, 3, 33, 950007, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservedbook',
            name='returned_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 2, 3, 33, 950007, tzinfo=utc)),
        ),
    ]
