# Generated by Django 2.2 on 2022-10-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_add_products_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Название')),
                ('description', models.TextField(max_length=10000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'акция',
                'verbose_name_plural': 'акции',
            },
        ),
    ]
