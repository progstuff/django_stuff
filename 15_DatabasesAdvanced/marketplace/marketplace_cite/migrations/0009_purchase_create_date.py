# Generated by Django 4.1.3 on 2022-11-17 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace_cite', '0008_basketitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата покупки'),
        ),
    ]
