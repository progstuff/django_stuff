from django.urls import path

from .views import RandomToDoView

urlpatterns = [
    path('', RandomToDoView.as_view(), name='todo-view'),
]
