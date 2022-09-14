from django.shortcuts import render
from django.views import View


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
