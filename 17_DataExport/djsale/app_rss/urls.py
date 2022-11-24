from django.urls import path
from .feeds import LatestEntriesFeed

urlpatterns = [
    path('latest/feed/', LatestEntriesFeed()),
]