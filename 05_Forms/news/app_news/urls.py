from django.urls import path
from . import views

urlpatterns = [
    path('all-news', views.NewsListView.as_view(), name='show_news'),
    path('change-news/<int:news_id>', views.NewsUpdateView.as_view(), name='change_news'),
    path('change-news/create', views.NewsCreateView.as_view(), name='create_news'),
    path('all-news/<int:news_id>/comments', views.CommentsListView.as_view(), name='comments'),
]
