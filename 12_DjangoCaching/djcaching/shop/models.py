from django.db import models
from django.utils.translation import gettext_lazy as _


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
    price = models.FloatField(default=0, verbose_name=_('Цена'))
    shop = models.ForeignKey(Shop, default=None, null=True, on_delete=models.CASCADE,
                             related_name="item_shop", verbose_name=_('Магазин'))

    class Meta:
        verbose_name_plural = _('товары')
        verbose_name = _('товар')

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))
    description = models.TextField(max_length=10000, verbose_name=_('Описание'))

    class Meta:
        verbose_name_plural = _('акции')
        verbose_name = _('акция')

    def __str__(self):
        return self.name