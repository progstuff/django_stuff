from django.http import HttpResponse

from django.views import View
from random import shuffle

class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python</li>'
                            '<li>Установить django</li>'
                            '<li>Запустить сервер</li>'
                            '<li>Порадоваться результату</li>'
                            '</ul>')


class RandomToDoView(View):

    def get_page_with_mixed_tasks(self):
        tasks = ['Задача 1', 'Задача 2', 'Задача 3', 'Задача 4', 'Задача 5']
        shuffle(tasks)
        page = '<ul>\n'
        for task in tasks:
            page += '\t<li>{}</li>\n'.format(task)
        page += '</ul>'
        return page

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.get_page_with_mixed_tasks())
