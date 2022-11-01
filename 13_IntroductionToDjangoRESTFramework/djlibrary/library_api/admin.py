from django.contrib import admin
from .models import Author, Book, AuthorRights


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'year', 'pages_cnt']


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name']


@admin.register(AuthorRights)
class AuthorRightsModelAdmin(admin.ModelAdmin):
    list_display = ['book', 'author']
