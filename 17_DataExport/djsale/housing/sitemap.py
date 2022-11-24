from django.contrib.sitemaps import Sitemap
from housing.models import News
from django.urls import reverse


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created_date


class ContactsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        data = list()
        data.append(ContactUrl())
        return data

    def lastmod(self, obj):
        return ''


class AboutSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        data = list()
        data.append(AboutUrl())
        return data

    def lastmod(self, obj):
        return ''


class ContactUrl:
    def get_absolute_url(self):
        return reverse('contacts')


class AboutUrl:
    def get_absolute_url(self):
        return reverse('about')