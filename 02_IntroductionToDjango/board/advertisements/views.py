from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def advertisements_list(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>Объявления</li>'
                        '</ul>')


def first_advertisement(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>1</li>'
                        '</ul>')


def second_advertisement(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>2</li>'
                        '</ul>')


def third_advertisement(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>3</li>'
                        '</ul>')


def fourth_advertisement(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>4</li>'
                        '</ul>')


def fifth_advertisement(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>5</li>'
                        '</ul>')