# Generated by Django 4.2.5 on 2024-03-07 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0034_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 5, 44, 31, 380456, tzinfo=datetime.timezone.utc)),
        ),
    ]
