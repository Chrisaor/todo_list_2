# Generated by Django 2.0.6 on 2018-06-14 00:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 14, 0, 45, 38, 511330, tzinfo=utc)),
        ),
    ]