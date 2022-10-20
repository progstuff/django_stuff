from django.db import migrations
from random import randint

def fill_db(apps, schema_editor):
    shops = apps.get_model('shop', 'Shop')

    products = apps.get_model('shop', 'Product')
    products.objects.all().delete()

    for j in range(1, 20):
        shop = shops.objects.get(name='Магазин № {}'.format(j))
        for i in range(1, randint(2, 20)):
            products.objects.create(name='Товар № {}'.format(i),
                                    description='Описание для товара № {} '.format(i),
                                    price=randint(3000, 10000)/100.0,
                                    shop=shop)


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20221020_2239'),
    ]

    operations = [migrations.RunPython(fill_db)]
