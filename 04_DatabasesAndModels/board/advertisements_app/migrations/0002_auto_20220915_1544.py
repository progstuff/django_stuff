# Generated by Django 2.2 on 2022-09-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='close_date',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='views_cnt',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.CharField(max_length=10000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(default='', max_length=1000, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='advertisementcategory',
            name='name',
            field=models.CharField(max_length=12, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(max_length=100, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='телефон'),
        ),
    ]
