# Generated by Django 2.2 on 2022-10-20 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Product',
        ),
    ]