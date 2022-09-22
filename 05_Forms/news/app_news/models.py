from django.db import models


class News(models.Model):

    title = models.CharField(max_length=1000, default='', verbose_name='заголовок')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100, default='', verbose_name='Пользователь')
    description = models.TextField(max_length=10000, verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                             related_name="news", verbose_name='Новость')

    def __str__(self):
        return self.user_name

