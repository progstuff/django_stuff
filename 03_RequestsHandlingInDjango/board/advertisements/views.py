from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class AdvertisementsView(View):
    cnt = 0
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]

    def get(self, request):

        AdvertisementsView.cnt = AdvertisementsView.cnt + 1
        return render(request,
                      'advertisements/advertisements_list.html',
                      {'advertisements': AdvertisementsView.advertisements,
                       'cnt': AdvertisementsView.cnt,
                       'type': 'GET'})

    def post(self, request):
        message = "запрос успешно выполнен"
        return render(request, 'advertisements/advertisements_list.html', {'message': message,
                                                                           'cnt': AdvertisementsView.cnt,
                                                                           'type': 'POST'})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = "адрес"
        context['phone'] = "8-xxx-xxx-xx-xx"
        context['email'] = "mail@mail.ru"
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Название компании"
        context['description'] = "описание компании "*200
        return context


class MainPage(TemplateView):
    template_name = 'advertisements/main_page.html'

    def get_context_data(self, **kwargs):
        regions = []
        categories = []
        for i in range(1, 20):
            regions.append("регион " + str(i))
            categories.append("категория " + str(i))

        context = super().get_context_data(**kwargs)
        context['regions'] = regions
        context['categories'] = categories
        return context
