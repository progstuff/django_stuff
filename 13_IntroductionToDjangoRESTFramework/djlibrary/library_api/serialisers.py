from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'last_name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'isbn', 'year', 'pages_cnt']