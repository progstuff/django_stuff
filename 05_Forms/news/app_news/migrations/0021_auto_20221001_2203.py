# Generated by Django 2.2 on 2022-10-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0020_auto_20221001_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('p', 'опубликовано'), ('d', 'на рассмотрении')], default='p', max_length=1, verbose_name='Статус'),
        ),
    ]
