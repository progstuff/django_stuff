from django.shortcuts import render
from django.views.generic import View
from .models import Housing, News


class ContactsPage(View):

    def get(self, request):
        return render(request,
                      'housing/page_contacts.html',
                      context={})


class AboutPage(View):

    def get(self, request):
        return render(request,
                      'housing/page_about.html',
                      context={})


class HouseListPage(View):

    def get(self, request):
        houses = list(Housing.objects.select_related('house_type').select_related('rooms_number').all())
        return render(request,
                      'housing/page_house_list.html',
                      context={'houses': houses})


class NewsPage(View):

    def get(self, request):
        news = list(News.objects.all())
        return render(request,
                      'housing/page_news.html',
                      context={'news': news})

