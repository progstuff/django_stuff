from django.db import migrations
from random import randint
from django.contrib.auth.hashers import make_password


def fill_db(apps, schema_editor):

    authors = apps.get_model('library_api', 'Author')
    books = apps.get_model('library_api', 'Book')
    author_rules = apps.get_model('library_api', 'AuthorRules')
    all_authors = authors.objects.all()
    all_books = books.objects.all()
    for author in all_authors:
        ind = randint(0, all_books.count()-1)
        book = all_books[ind]
        author_rules.objects.create(author=author,
                            book=book)
        for i in range(3):
            chance = randint(0, 1)
            if chance == 1:
                ind = randint(0, all_books.count() - 1)
                book = all_books[ind]
                author_rules.objects.create(author=author,
                                            book=book)


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0004_remove_authorrules_author_remove_authorrules_book_and_more'),
    ]

    operations = [migrations.RunPython(fill_db)]
