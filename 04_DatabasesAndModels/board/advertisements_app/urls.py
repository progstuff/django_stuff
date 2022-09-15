from django.urls import path
from . import views

urlpatterns = [
    path('advertisements', views.AdvertisementsList.as_view(), name='main_page'),
]
