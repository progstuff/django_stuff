from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppTestLocaleConfig(AppConfig):
    name = 'app_test_locale'
    verbose_name = _('test model')
