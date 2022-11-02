from django.contrib import admin
from .models import Author, Book, AuthorRules


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'year', 'pages_cnt']


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name']


@admin.register(AuthorRules)
class AuthorRulesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'book']