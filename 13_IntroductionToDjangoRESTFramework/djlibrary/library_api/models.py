from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=1000, verbose_name=_('Фамилия'))

    class Meta:
        verbose_name_plural = _('Авторы')
        verbose_name = _('Автор')

    def __str__(self):
        return self.name + self.last_name


class Book(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_('Название'))
    isbn = models.CharField(max_length=1000, verbose_name=_('ISBN'))
    year = models.IntegerField(verbose_name=_('Год выпуска'))
    pages_cnt = models.IntegerField(verbose_name=_('К-во страниц'))

    class Meta:
        verbose_name_plural = _('Книги')
        verbose_name = _('Книга')

    def __str__(self):
        return self.name


class AuthorRights:
    book = models.ForeignKey(Book, default=None, null=True, on_delete=models.CASCADE,
                             related_name="book", verbose_name=_('Книга'))
    author = models.ForeignKey(Author, default=None, null=True, on_delete=models.CASCADE,
                               related_name="author", verbose_name=_('Автор'))

    class Meta:
        verbose_name_plural = _('Авторские права')
        verbose_name = _('Авторское право')

    def __str__(self):
        return self.book.__str__() + " " + self.author.__str__()