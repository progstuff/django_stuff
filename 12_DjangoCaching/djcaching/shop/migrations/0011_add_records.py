from django.db import migrations
from random import randint
from django.contrib.auth.hashers import make_password


def fill_db(apps, schema_editor):

    shops = apps.get_model('shop', 'Shop')
    shops.objects.all().delete()
    shops_cnt = 20
    for i in range(1, shops_cnt+1):
        shops.objects.create(name='Магазин № {}'.format(i),
                             addres=('Адрес магазина № {} '.format(i)))

    products = apps.get_model('shop', 'Product')
    products.objects.all().delete()

    products_cnt = 30
    for i in range(1, products_cnt+1):
        products.objects.create(name='Товар № {}'.format(i),
                                description='Описание для товара № {} '.format(i))

    products_in_shop = apps.get_model('shop', 'ProductInShop')

    for i in range(1, shops_cnt+1):
        products_in_shop_cnt = randint(5, products_cnt)
        for j in range(1, products_in_shop_cnt+1):
            products_in_shop.objects.create(shop=shops.objects.get(name='Магазин № {}'.format(i)),
                                            product=products.objects.get(name='Товар № {}'.format(j)),
                                            price=randint(1000, 3000)/10.0,
                                            count=randint(5, 20))

    users = apps.get_model('auth', 'User')
    users_cnt = 10
    for i in range(1, users_cnt+1):
        users.objects.create(username='User_{}'.format(i), password=make_password('User_{}'.format(i)))

    purchases = apps.get_model('shop', 'Purchase')
    for i in range(1, 10):
        user = users.objects.all()[randint(0, users_cnt - 1)]
        shop = shops.objects.all()[randint(0, shops_cnt - 1)]
        product_in_shop = products_in_shop.objects.filter(shop=shop).order_by('-id')[0]
        purchases.objects.create(user=user,
                                 shop=shop,
                                 product=product_in_shop.product,
                                 bought_price=product_in_shop.price,
                                 count=randint(2, 5))


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20221022_1658'),
    ]

    operations = [migrations.RunPython(fill_db)]
