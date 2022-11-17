from django.db import migrations
from datetime import datetime
from random import randint


def fill_db(apps, schema_editor):

    purchases = apps.get_model('marketplace_cite', 'Purchase')
    all_purchases = list(purchases.objects.all())
    for purchase in all_purchases:
        day = randint(1, 20)
        month = randint(1, 10)
        year = randint(2018, 2022)
        hours = randint(0, 23)
        minutes = randint(0, 59)
        seconds = randint(0, 59)
        purchase.create_date = datetime(year, month, day, hours, minutes, seconds)
        purchase.save()


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace_cite', '0009_purchase_create_date'),
    ]

    operations = [migrations.RunPython(fill_db)]
