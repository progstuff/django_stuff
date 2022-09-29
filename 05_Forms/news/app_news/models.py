from django.db import models
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User


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


class UserProfile(models.Model):
    VERIFICATION_STATUS_CHOICES = [
        (True, 'да'),
        (False, 'нет')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default=None, verbose_name='Телефон')
    town = models.CharField(max_length=100, default=None, verbose_name='Город')
    news_cnt = models.IntegerField(default=0, verbose_name='Количество новостей')
    verification = models.BooleanField(default=False, choices=VERIFICATION_STATUS_CHOICES, verbose_name='Верифицирован')

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = (
            ('usual_user', 'обычный пользователь'),
            ('verificated_user', 'верифицированный пользователь'),
            ('moderator', 'модератор')
        )


class Comment(models.Model):
    STATUS_CHOICES = [
        ('p', 'опубликовано'),
        ('d', 'удалено администратором')
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

