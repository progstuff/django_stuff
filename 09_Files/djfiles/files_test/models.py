from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             related_name="user_records", verbose_name='Пользователь')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title


class RecordFiles(models.Model):
    record = models.ForeignKey(Record, default=None, null=True, on_delete=models.CASCADE,
                               related_name="record", verbose_name='Запись')
    file = models.FileField(upload_to='files/', default=None, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default=None, verbose_name='Имя')
    last_name = models.CharField(max_length=50, default=None, verbose_name='Фамилия')
    about = models.TextField(max_length=500, default=None, verbose_name='О себе')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
