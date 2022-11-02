from rest_framework import routers
from .api import UserViewSet, AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
urlpatterns = router.urls
