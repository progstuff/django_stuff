from rest_framework import routers
from .api import UserViewSet, AuthorViewSet, BookViewSet
from django.urls import path


#router = routers.DefaultRouter()
#router.register('users', UserViewSet)
#router.register('books', BookViewSet)
#router.register('authors', AuthorViewSet)
#urlpatterns = router.urls
urlpatterns = [
    path('books/', BookViewSet.as_view(), name='authors'),
    path('authors/', AuthorViewSet.as_view(), name='authors'),
]
