from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    CHOICES = (
        ('З', 'Золото'),
        ('C', 'Серебро'),
        ('Б', 'Бронза'),
    )

    name = models.CharField(max_length=1000, verbose_name=_('Имя'))
    balance = models.FloatField(verbose_name=_('Баланс'))
    status = models.CharField(max_length=1000, choices=CHOICES, verbose_name=_('Статус'))
    user = models.ForeignKey(User, default=None, null=False, on_delete=models.CASCADE,
                             related_name="users", verbose_name=_('Пользователь'))


class Shop(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))


class Product(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))
    description = models.CharField(max_length=1000, verbose_name=_('Описание'))


class Purchase(models.Model):
    shop = models.ForeignKey(Shop, default=None, null=False, on_delete=models.DO_NOTHING,
                             related_name="shops", verbose_name=_('Магазин'))

    product = models.ForeignKey(Product, default=None, null=False, on_delete=models.DO_NOTHING,
                                related_name="products", verbose_name=_('Товар'))

    user = models.ForeignKey(UserProfile, default=None, null=False, on_delete=models.DO_NOTHING,
                             related_name="users_profiles", verbose_name=_('Профиль пользователя'))

    count = models.IntegerField(default=0, verbose_name=_('Количество'))

    price = models.FloatField(default=0, verbose_name=_('Цена'))


class Storage(models.Model):
    shop = models.ForeignKey(Shop, default=None, null=False, on_delete=models.DO_NOTHING,
                             related_name="storage_shops", verbose_name=_('Магазин'))
    product = models.ForeignKey(Product, default=None, null=False, on_delete=models.DO_NOTHING,
                                related_name="storage_products", verbose_name=_('Товар'))
    count = models.IntegerField(default=0, verbose_name=_('Количество'))

    price = models.FloatField(default=0, verbose_name=_('Цена'))