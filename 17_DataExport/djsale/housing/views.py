from django.shortcuts import render
from django.views.generic import View
# Create your views here.


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
        return render(request,
                      'housing/page_house_list.html',
                      context={})


class NewsPage(View):

    def get(self, request):
        return render(request,
                      'housing/page_news.html',
                      context={})

