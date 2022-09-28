from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LogInView.as_view(), name='login'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('all-news', views.NewsListView.as_view(), name='show_news'),
    path('change-news/<int:news_id>', views.NewsUpdateView.as_view(), name='change_news'),
    path('change-news/create', views.NewsCreateView.as_view(), name='create_news'),
    path('all-news/<int:news_id>/comments', views.CommentsListView.as_view(), name='comments'),
    path('register', views.RegisterView.as_view(), name='register_user'),
    path('user_page', views.UserPage.as_view(), name='user_page'),
]
