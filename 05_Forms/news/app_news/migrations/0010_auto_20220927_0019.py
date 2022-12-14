# Generated by Django 2.2 on 2022-09-26 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0009_auto_20220924_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_anonim',
            field=models.BooleanField(default=False, verbose_name='Анонимный'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(choices=[(True, 'активная'), (False, 'не активная')], default=True, verbose_name='Активна'),
        ),
    ]
