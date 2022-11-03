from rest_framework import serializers
from django.contrib.auth.models import User
from.models import Book, Author


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# Serializers define the API representation.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'year', 'pages_cnt']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'last_name', 'books']

