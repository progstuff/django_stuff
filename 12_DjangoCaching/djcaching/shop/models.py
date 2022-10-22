from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime


class Shop(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))
    addres = models.CharField(max_length=1000, verbose_name=_('Адрес'))

    class Meta:
        verbose_name_plural = _('магазины')
        verbose_name = _('магазин')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))
    description = models.TextField(max_length=10000, verbose_name=_('Описание'))

    class Meta:
        verbose_name_plural = _('товары')
        verbose_name = _('товар')

    def __str__(self):
        return self.name


class ProductInShop(models.Model):
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.CASCADE,
                                related_name="item_shop", verbose_name=_('Товар'))
    shop = models.ForeignKey(Shop, default=None, null=True, on_delete=models.CASCADE,
                             related_name="shop", verbose_name=_('Магазин'))
    price = models.FloatField(default=0, verbose_name=_('Цена'))
    count = models.IntegerField(default=0, verbose_name=_('Количество'))


class Purchase(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             related_name="user", verbose_name=_('Пользователь'))
    product = models.ForeignKey(Product, default=None, null=True, on_delete=models.CASCADE,
                                related_name="item_user", verbose_name=_('Товар'))
    shop = models.ForeignKey(Shop, default=None, null=True, on_delete=models.CASCADE,
                             related_name="shop_user", verbose_name=_('Магазин'))
    bought_price = models.FloatField(default=0, verbose_name=_('Цена'))
    count = models.IntegerField(default=0, verbose_name=_('Количество'))
    create_date = models.DateTimeField(default=datetime.now, verbose_name='Дата покупки')

    def __str__(self):
        return self.product.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             related_name="user_for_profile", verbose_name=_('Пользователь'))
    balance = models.FloatField(default=0, verbose_name=_('Баланс'))


class Discount(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))
    description = models.TextField(max_length=10000, verbose_name=_('Описание'))

    class Meta:
        verbose_name_plural = _('акции')
        verbose_name = _('акция')

    def __str__(self):
        return self.name
