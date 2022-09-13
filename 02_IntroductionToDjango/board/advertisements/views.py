from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def advertisements_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisements_list.html', {})


def first_advertisement(request, *args, **kwargs):
    return render(request, 'advertisements/first_advertisement.html', {})


def second_advertisement(request, *args, **kwargs):
    return render(request, 'advertisements/second_advertisement.html', {})


def third_advertisement(request, *args, **kwargs):
    return render(request, 'advertisements/third_advertisement.html', {})


def fourth_advertisement(request, *args, **kwargs):
    return render(request, 'advertisements/fourth_advertisement.html', {})


def fifth_advertisement(request, *args, **kwargs):
    return render(request, 'advertisements/fifth_advertisement.html', {})