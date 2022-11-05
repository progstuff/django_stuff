from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from .serialisers import UserSerializer, BookSerializer, AuthorSerializer
from .models import Book, Author


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(generics.ListCreateAPIView):
    """ Представление для получения списка книг"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        pages_min = self.request.query_params.get('pages_min', None)
        pages_max = self.request.query_params.get('pages_max', None)
        pages_equal = self.request.query_params.get('pages_equal', None)
        author_name = self.request.query_params.get('author', None)
        book_title = self.request.query_params.get('title', None)

        if pages_min is not None:
            try:
                val = int(pages_min)
                queryset = queryset.filter(pages_cnt__gt=val)
            except ValueError:
                print(pages_min, 'не удалось преобразовать в число')
        if pages_max is not None:
            try:
                val = int(pages_max)
                queryset = queryset.filter(pages_cnt__lt=val)
            except ValueError:
                print(pages_min, 'не удалось преобразовать в число')
        if pages_equal is not None:
            try:
                val = int(pages_equal)
                queryset = queryset.filter(pages_cnt=val)
            except ValueError:
                print(pages_min, 'не удалось преобразовать в число')
        if author_name is not None and book_title is not None:
            queryset = queryset.filter(author__name=author_name, name=book_title)

        return queryset


class AuthorViewSet(generics.ListCreateAPIView):
    """ Представление для получения списка авторов"""
    model = Author
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
