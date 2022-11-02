from django.db import migrations
from random import randint
from django.contrib.auth.hashers import make_password


def fill_db(apps, schema_editor):

    authors = apps.get_model('library_api', 'Author')
    books = apps.get_model('library_api', 'Book')
    authors_cnt = 10
    for i in range(authors_cnt):
        authors.objects.create(name="Name {}".format(i+1), last_name="Lastname {}".format(i+1))

    books_cnt = 20
    for i in range(books_cnt):
        books.objects.create(name="Title {}".format(i+1),
                             isbn="Code {}".format(i+1),
                             year=randint(1990, 2020),
                             pages_cnt=randint(50, 500))


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0001_initial'),
    ]

    operations = [migrations.RunPython(fill_db)]
