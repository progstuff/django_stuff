from django.db import migrations
from random import randint
from django.contrib.auth.hashers import make_password


def fill_db(apps, schema_editor):

    users = apps.get_model('auth', 'User')
    user_profiles = apps.get_model('marketplace_cite', 'UserProfile')
    shops = apps.get_model('marketplace_cite', 'Shop')
    products = apps.get_model('marketplace_cite', 'Product')
    purchases = apps.get_model('marketplace_cite', 'Purchase')
    storages = apps.get_model('marketplace_cite', 'Storage')
    users_cnt = 10
    shops_cnt = 20
    products_cnt = 30
    max_storages_cnt = 20
    min_storages_cnt = 5
    min_product_count = 10
    max_product_count = 100
    min_product_price = 100
    max_product_price = 400
    min_balance = 100
    max_balance = min_balance*50
    min_purchases_cnt = 10
    max_purchases_cnt = 20

    for user_ind in range(1, users_cnt+1):
        users.objects.create(username='User_{}'.format(user_ind),
                             password=make_password('User_{}'.format(user_ind)))
    print('Users added')
    for ind, user in enumerate(users.objects.all()):
        user_profiles.objects.create(name='name_in_profile{}'.format(ind+1),
                                     balance=randint(min_balance*100, max_balance*100)/100.0,
                                     status='Б',
                                     user=user)
    print('User profiles added')
    for shop_ind in range(1, shops_cnt+1):
        shops.objects.create(name='shop_{}'.format(shop_ind))
    print('Shops added')
    for product_ind in range(1, products_cnt+1):
        products.objects.create(name='product_{}'.format(product_ind),
                                description='description_{}'.format(product_ind))
    print('Products added')
    all_products = products.objects.all()
    for ind, shop in enumerate(shops.objects.all()):
        choosed_products = []
        storages_cnt = randint(min_storages_cnt, max_storages_cnt)
        for storage_ind in range(storages_cnt):
            while True:
                product_ind = randint(0, products_cnt-1)
                if product_ind not in choosed_products:
                    choosed_products.append(product_ind)
                    break

            product = all_products[product_ind]
            storages.objects.create(shop=shop,
                                    product=product,
                                    count=randint(min_product_count, max_product_count),
                                    price=randint(min_product_price*100, max_product_price*100)/100)
        print('Add {0} storages for {1} shop'.format(storages_cnt, ind+1))

    all_user_profiles = user_profiles.objects.all()
    all_storages = storages.objects.all()
    for ind, user_profile in enumerate(all_user_profiles):
        purchases_cnt = randint(min_purchases_cnt, max_purchases_cnt)
        for purchase_ind in range(purchases_cnt):
            storage_ind = randint(0, len(all_storages) - 1)

            storage = all_storages[storage_ind]
            purchases.objects.create(shop=storage.shop,
                                     product=storage.product,
                                     user=user_profile,
                                     count=randint(1, 10),
                                     price=storage.price)
        print('Add {0} purchases for user {1}'.format(purchases_cnt, ind + 1))


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace_cite', '0001_initial'),
    ]

    operations = [migrations.RunPython(fill_db)]
