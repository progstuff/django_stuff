from django.views import generic
from advertisements_app.models import Advertisement


class AdvertisementsListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements_app/advertisements_list.html'
    context_object_name = 'advertisements'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisements_app/advertisement_detail.html'
    context_object_name = 'advertisement'

    def get_object(self):
        obj = super().get_object()
        obj.views_cnt += 1
        obj.save()
        return obj
