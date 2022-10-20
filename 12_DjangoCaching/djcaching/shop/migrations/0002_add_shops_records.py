from django.db import migrations


def fill_db(apps, schema_editor):
    shops = apps.get_model('shop', 'Shop')
    shops.objects.all().delete()
    for i in range(1, 20):
        shops.objects.create(name='Магазин № {}'.format(i),
                             addres=('Адрес магазина № {} '.format(i)))


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [migrations.RunPython(fill_db)]
