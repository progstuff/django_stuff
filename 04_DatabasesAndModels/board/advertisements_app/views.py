from django.views.generic import TemplateView

class AdvertisementsList(TemplateView):
    template_name = 'advertisements_app/advertisements_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = "адрес"
        context['phone'] = "8-xxx-xxx-xx-xx"
        context['email'] = "mail@mail.ru"
        return context