from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default=None, verbose_name='Имя')
    last_name = models.CharField(max_length=50, default=None, verbose_name='Фамилия')
    about = models.TextField(max_length=500, default=None, verbose_name='О себе')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)