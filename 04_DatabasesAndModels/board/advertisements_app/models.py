from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, default='', verbose_name='заголовок')
    price = models.FloatField(verbose_name='Цена')
    description = models.CharField(max_length=10000, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views_cnt = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True, on_delete=models.CASCADE,
                                 related_name="categories")
    author = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.CharField(max_length=100, verbose_name='e-mail')
    phone = models.CharField(max_length=100, verbose_name='телефон')


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=12, verbose_name='Категория')



