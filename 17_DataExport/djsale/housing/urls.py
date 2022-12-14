from django.urls import path
from . import views


urlpatterns = [
    path('contacts', views.ContactsPage.as_view(), name='contacts'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('news', views.NewsPage.as_view(), name='news'),
    path('news-item/<int:pk>', views.NewsItemPage.as_view(), name='news-item'),
    path('house-list', views.HouseListPage.as_view(), name='house-list')
]