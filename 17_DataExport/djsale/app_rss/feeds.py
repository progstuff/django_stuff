from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from housing.models import News


class LatestEntriesFeed(Feed):
    title = _("Новости")
    link = "/sitenews/"
    description = _("Последние новости")

    def items(self):
        return News.objects.order_by('-created_date')[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])