from django.urls import path
from .import views

urlpatterns = [
    path("", views.advertisements_list, name="advertisements_list"),
    path("first_advertisement", views.first_advertisement, name="first_advertisement"),
    path("second_advertisement", views.second_advertisement, name="second_advertisement"),
    path("third_advertisement", views.third_advertisement, name="third_advertisement"),
    path("fourth_advertisement", views.fourth_advertisement, name="fourth_advertisement"),
    path("fifth_advertisement", views.fifth_advertisement, name="fifth_advertisement")
]