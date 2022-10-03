from django.db import models
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User


class News(models.Model):
    STATUS_CHOICES = [
        (True, 'активная'),
        (False, 'не активная')
    ]
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             related_name="user_news", verbose_name='Пользователь')
    title = models.CharField(max_length=1000, default='', verbose_name='заголовок')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, choices=STATUS_CHOICES, verbose_name='Активна')
    tag = models.CharField(default='', max_length=10, verbose_name='Тег')

    def __str__(self):
        return self.title



class UserProfile(models.Model):
    STATUS_CHOICES = [
        (True, 'да'),
        (False, 'нет')
    ]
    USER_STATE = [
        (0, 'Обычный пользователь'),
        (1, 'Верифицированный пользователь'),
        (2, 'Модератор')
    ]
    USER_REQUESTS = [
        (0, 'Нет'),
        (1, 'Запрос верификации'),
        (2, 'Стать модератором')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default=None, verbose_name='Телефон')
    town = models.CharField(max_length=100, default=None, verbose_name='Город')
    news_cnt = models.IntegerField(default=0, verbose_name='Количество новостей')
    user_state = models.IntegerField(default=0, choices=USER_STATE, verbose_name='Статус')
    user_request = models.IntegerField(default=0, choices=USER_REQUESTS, verbose_name='Запрос')

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = (
            ('usualuser', 'обычный пользователь'),
            ('verificateduser', 'верифицированный пользователь'),
            ('moderator', 'модератор')
        )


class Comment(models.Model):
    STATUS_CHOICES = [
        ('p', 'опубликовано'),
        ('d', 'на рассмотрении')
    ]

    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             related_name="user", verbose_name='Пользователь')
    description = models.TextField(max_length=10000, verbose_name='Комментарий')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                             related_name="news", verbose_name='Новость')

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p', verbose_name='Статус')
    is_anonim = models.BooleanField(default=False, verbose_name='Анонимный')

    @property
    def short_description(self):
        return truncatechars(self.description, 15)
    short_description.fget.short_description = 'Комментарий'

    def __str__(self):
        return self.user.__str__()

