from django.db import migrations
from random import randint
from django.contrib.auth.hashers import make_password


def fill_db(apps, schema_editor):

    users = apps.get_model('auth', 'User')
    user_profiles = apps.get_model('shop', 'UserProfile')
    all_users = users.objects.all()
    for user in all_users:
        user_profiles.objects.create(user=user, balance=randint(10000, 100000)/10.0)


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_userprofile'),
    ]

    operations = [migrations.RunPython(fill_db)]
