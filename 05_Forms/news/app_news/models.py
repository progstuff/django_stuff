from django.db import models
from django.template.defaultfilters import truncatechars


class News(models.Model):
    STATUS_CHOICES = [
        (True, 'активная'),
        (False, 'не активная')
    ]
    title = models.CharField(max_length=1000, default='', verbose_name='заголовок')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, choices=STATUS_CHOICES, verbose_name='Активна')

    def __str__(self):
        return self.title


class User(models.Model):

    user_name = models.CharField(max_length=100, default='', verbose_name='Пользователь')

    def __str__(self):
        return self.user_name


class Comment(models.Model):
    STATUS_CHOICES = [
        ('p', 'опубликовано'),
        ('d', 'удалено администратором')
    ]

    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE,
                             related_name="user", verbose_name='Пользователь')
    description = models.TextField(max_length=10000, verbose_name='Комментарий')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                             related_name="news", verbose_name='Новость')

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p', verbose_name='Статус')

    @property
    def short_description(self):
        return truncatechars(self.description, 15)
    short_description.fget.short_description = 'Комментарий'

    def __str__(self):
        return self.user.__str__()

