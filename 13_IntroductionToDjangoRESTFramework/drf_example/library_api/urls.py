from rest_framework import routers
from .api import UserViewSet, AuthorViewSet, BookViewSet
from django.urls import path


urlpatterns = [
    path('books/', BookViewSet.as_view(), name='authors'),
    path('authors/', AuthorViewSet.as_view(), name='authors'),
]
