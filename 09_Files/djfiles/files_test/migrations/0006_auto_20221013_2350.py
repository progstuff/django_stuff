# Generated by Django 2.2 on 2022-10-13 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files_test', '0005_auto_20221013_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='create_date',
            field=models.DateField(default=datetime.date(2022, 10, 13), verbose_name='Дата создания'),
        ),
    ]
