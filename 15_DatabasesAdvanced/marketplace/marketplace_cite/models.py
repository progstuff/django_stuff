from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    CHOICES = (
        ('З', 'Золото'),
        ('C', 'Серебро'),
        ('Б', 'Бронза'),
    )

    name = models.CharField(max_length=1000, verbose_name=_('Имя'))
    balance = models.FloatField(verbose_name=_('Баланс'))
    status = models.CharField(max_length=1000, choices=CHOICES, verbose_name=_('Статус'))
    user = models.OneToOneField(User, default=None, null=False, on_delete=models.CASCADE,
                                related_name="users", verbose_name=_('Пользователь'))

    class Meta:
        verbose_name_plural = _('Профили пользователей')
        verbose_name = _('Профиль пользователя')

    def __str__(self):
        return self.user.username + " " + self.name


class Shop(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))

    class Meta:
        verbose_name_plural = _('Магазины')
        verbose_name = _('магазин')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))
    description = models.CharField(max_length=1000, verbose_name=_('Описание'))

    class Meta:
        verbose_name_plural = _('Товары')
        verbose_name = _('товар')

    def __str__(self):
        return self.name


class Purchase(models.Model):
    shop = models.ForeignKey(Shop, default=None, null=False, on_delete=models.DO_NOTHING,
                             related_name="shops", verbose_name=_('Магазин'))

    product = models.ForeignKey(Product, default=None, null=False, on_delete=models.DO_NOTHING,
                                related_name="products", verbose_name=_('Товар'))

    user = models.ForeignKey(UserProfile, default=None, null=False, on_delete=models.DO_NOTHING,
                             related_name="users_profiles", verbose_name=_('Профиль пользователя'))

    count = models.IntegerField(default=0, verbose_name=_('Количество'))

    price = models.FloatField(default=0, verbose_name=_('Цена'))

    create_date = models.DateTimeField(default=datetime.now, verbose_name='Дата покупки')

    class Meta:
        verbose_name_plural = _('Покупки')
        verbose_name = _('покупку')

    def __str__(self):
        return self.product.name + " " + self.shop.name


class Storage(models.Model):
    shop = models.ForeignKey(Shop, default=None, null=False, on_delete=models.DO_NOTHING,
                             related_name="storage_shops", verbose_name=_('Магазин'))
    product = models.ForeignKey(Product, default=None, null=False, on_delete=models.DO_NOTHING,
                                related_name="storage_products", verbose_name=_('Товар'))
    count = models.IntegerField(default=0, verbose_name=_('Количество'))

    price = models.FloatField(default=0, verbose_name=_('Цена'))

    class Meta:
        verbose_name_plural = _('Склады')
        verbose_name = _('склад')

    def __str__(self):
        return self.shop.name + self.product.name


class BasketItem(models.Model):
    user = models.ForeignKey(UserProfile, default=None, null=False, on_delete=models.CASCADE,
                             related_name="users_bascket", verbose_name=_('Пользователь'))
    storage = models.ForeignKey(Storage, default=None, null=False, on_delete=models.CASCADE,
                                related_name="users_purchases", verbose_name=_('Товар'))
    count = models.IntegerField(default=0, verbose_name=_('Количество'))
    price = models.FloatField(default=0, verbose_name=_('Цена'))

    class Meta:
        verbose_name_plural = _('Корзины')
        verbose_name = _('корзина')

    def __str__(self):
        return self.shop.name + self.product.name