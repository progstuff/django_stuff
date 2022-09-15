# Generated by Django 2.2 on 2022-09-15 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0003_advertisement_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.Author'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='advertisements_app.AdvertisementCategory'),
        ),
    ]
