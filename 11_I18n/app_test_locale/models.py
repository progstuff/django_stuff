from django.db import models
from django.utils.translation import gettext_lazy as _


class TestModel(models.Model):
    field_one = models.CharField(max_length=100, verbose_name=_('field one'))
    field_two = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('field two'))

    class Meta:
        verbose_name_plural = _('rows')
        verbose_name = _('row')