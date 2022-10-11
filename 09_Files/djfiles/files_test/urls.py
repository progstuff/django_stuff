from django.urls import path
from . import views

urlpatterns = [
    path('all-posts', views.AllPosts.as_view(), name='all-posts'),
    path('post-details/<int:post_id>', views.PostDetails.as_view(), name='post-details'),
    path('register-user', views.RegisterPage.as_view(), name='register-user'),
    path('login', views.LogInView.as_view(), name='login-user'),
    path('logout', views.LogOutView.as_view(), name='logout-user'),
    path('user-page', views.UserPage.as_view(), name='user-page'),
    path('create-post', views.PostCreate.as_view(), name='create-post'),
]