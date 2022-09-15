from django.urls import path
from .views import AdvertisementsListView, AdvertisementDetailView

urlpatterns = [
    path('advertisements', AdvertisementsListView.as_view(), name='main_page'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='detail_page'),
]
