from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_name, name='main_page'),
    path('all-news', views.AdvertisementsListView.as_view(), name='show_news'),
    path('create-news', views.create_news, name='create_news'),
    path('change-news/<int:pk>', views.NewsDetailView.as_view(), name='change_news'),

    path('all-news/<int:pk>/comments', views.CommentsListView.as_view(), name='comments'),


]
