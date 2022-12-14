# Generated by Django 2.2 on 2022-09-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0017_auto_20220930_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_request',
            field=models.IntegerField(choices=[(0, 'Нет'), (1, 'Запрос верификации'), (2, 'Стать модератором')], default=0, verbose_name='Запрос'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_state',
            field=models.IntegerField(choices=[(0, 'Обычный пользователь'), (1, 'Верифицированный пользователь'), (2, 'Модератор')], default=0, verbose_name='Статус'),
        ),
    ]
