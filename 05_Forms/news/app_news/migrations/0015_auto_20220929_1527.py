# Generated by Django 2.2 on 2022-09-29 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0013_auto_20220928_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('usual_user', 'обычный пользователь'), ('verificated_user', 'верифицированный пользователь'), ('moderator', 'модератор'))},
        ),
    ]