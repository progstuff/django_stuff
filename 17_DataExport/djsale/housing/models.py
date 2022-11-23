from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Заголовок'))
    description = models.TextField(max_length=10000, verbose_name=_('Описание'))

    class Meta:
        verbose_name_plural = _('Новости')
        verbose_name = _('Новость')

    def __str__(self):
        return self.name


class HouseType(models.Model):
    type_name = models.CharField(max_length=1000, verbose_name=_('Тип жилья'))

    class Meta:
        verbose_name_plural = _('Типы помещений')
        verbose_name = _('Тип помещения')

    def __str__(self):
        return self.type_name


class RoomsNumber(models.Model):
    number_type = models.CharField(max_length=1000, verbose_name=_('Количество комнат'))

    class Meta:
        verbose_name_plural = _('Количество комнат')
        verbose_name = _('Количество комнат')

    def __str__(self):
        return self.number_type


class Housing(models.Model):
    address = models.CharField(max_length=1000, verbose_name=_('адрес'))
    house_type = models.ForeignKey(HouseType, default=None, null=True, on_delete=models.CASCADE,
                                   related_name="house_type", verbose_name=_('тип жилья'))
    rooms_number = models.ForeignKey(RoomsNumber, default=None, null=True, on_delete=models.CASCADE,
                                     related_name="rooms_number", verbose_name=_('количество комнат'))

    class Meta:
        verbose_name_plural = _('Квартиры')
        verbose_name = _('Жильё')

    def __str__(self):
        return self.address + " " + self.house_type.type_name + " " + self.rooms_number.number_type