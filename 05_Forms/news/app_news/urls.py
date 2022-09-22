from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_name, name='main_page'),
    path('all-news', views.show_all_news, name='show_news'),
    path('create-news', views.create_news, name='create_news'),
    path('change-news', views.change_news, name='change_news'),
    path('comments', views.show_comments, name='comments'),


]
