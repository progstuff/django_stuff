from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('advertisements/', views.AdvertisementsView.as_view(), name='advertisements_list'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
]
