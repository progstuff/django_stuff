from django.contrib import admin
from .models import Author, Book


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'year', 'pages_cnt', 'author']


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name']
