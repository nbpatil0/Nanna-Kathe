# Generated by Django 3.0.3 on 2020-04-18 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20200417_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='start_date',
            field=models.DateField(default=datetime.date(2020, 4, 18)),
        ),
    ]
