# Generated by Django 3.2.7 on 2021-10-14 01:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0013_auto_20211011_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservedbook',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 1, 48, 4, 894327, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservedbook',
            name='returned_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 1, 48, 4, 894327, tzinfo=utc)),
        ),
    ]
