# Generated by Django 4.0.2 on 2022-02-13 13:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 13, 35, 53, 791769, tzinfo=utc)),
        ),
    ]
