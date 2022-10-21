from django.db import migrations


def fill_db(apps, schema_editor):

    discounts = apps.get_model('shop', 'Discount')
    discounts.objects.all().delete()

    for i in range(1, 5):
        discounts.objects.create(name='Акция № {}'.format(i),
                                 description='Описание для акции № {} '.format(i))


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_discount'),
    ]

    operations = [migrations.RunPython(fill_db)]
