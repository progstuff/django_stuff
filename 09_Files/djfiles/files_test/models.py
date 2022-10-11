from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             related_name="user_records", verbose_name='Пользователь')
    title = models.CharField(max_length=100, default='', verbose_name='заголовок')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title
