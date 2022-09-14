from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdvertisementsView.as_view(), name='advertisements_list'),
]
