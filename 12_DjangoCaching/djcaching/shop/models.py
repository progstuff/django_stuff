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



