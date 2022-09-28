# Generated by Django 2.2 on 2022-09-22 10:49

from django.db import migrations
from random import randint


def fill_db(apps, schema_editor):
    news = apps.get_model('app_news', 'News')
    news.objects.all().delete()
    for i in range(1, 20):
        news.objects.create(title='Новость {}'.format(i),
                            description=('Описание {} '.format(i))*30,
                            is_active=True)

    comments = apps.get_model('app_news', 'Comment')
    comments.objects.all().delete()

    users = apps.get_model('auth', 'User')
    users_profiles = apps.get_model('app_news', 'UserProfile')
    for i in range(1, 5):
        users.objects.create(username='User_{}'.format(i), password='User_{}'.format(i))
        user = users.objects.get(username='User_{}'.format(i))
        users_profiles.objects.create(user=user, phone=str(i)*10, town='Город {}'.format(i))


    for i in range(1, 20):
        for j in range(1, randint(2, 10)):
            user_name = 'User_{}'.format(randint(1, 4))
            comments.objects.create(user=users.objects.get(username=user_name),
                                    description='Комментарий {}'.format(j),
                                    news=news.objects.get(title='Новость {}'.format(i)))


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0013_auto_20220928_1608'),
    ]

    operations = [migrations.RunPython(fill_db)]
