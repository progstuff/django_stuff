from django.db import migrations
from random import randint
from django.contrib.auth.hashers import make_password


def fill_db(apps, schema_editor):

    authors = apps.get_model('library_api', 'Author')
    books = apps.get_model('library_api', 'Book')
    authors_cnt = 10
    for i in range(authors_cnt):
        authors.objects.create(name="Name {}".format(i+1), last_name="Lastname {}".format(i+1))
    all_authors = authors.objects.all()
    books_cnt = 20
    for i in range(books_cnt):
        ind = randint(0, all_authors.count() - 1)
        author = all_authors[ind]
        books.objects.create(name="Title {}".format(i+1),
                             isbn="Code {}".format(i+1),
                             year=randint(1990, 2020),
                             pages_cnt=randint(50, 500),
                             author=author)


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0005_book_author_delete_authorrules'),
    ]

    operations = [migrations.RunPython(fill_db)]
