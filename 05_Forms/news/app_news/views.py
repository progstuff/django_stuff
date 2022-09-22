
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Comment
from .forms import NewsForm, CommentForm
from django.views import generic, View


class NewsListView(View):

    def get(self, request):
        news = News.objects.all().order_by('-create_date')
        return render(request, 'app_news/show_news.html', context={'all_news': news})

    def post(self, request):
        return HttpResponseRedirect('change-news/create')


class NewsUpdateView(View):

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/change_news.html', context={'button_name': 'Создать',
                                                                     'title': 'Создать новость',
                                                                     'news_form': news_form})

    def post(self, request, news_id):
        news_form = NewsForm(request.POST)
        news = News.objects.get(id=news_id)
        if news_form.is_valid():
            news.title = request.POST['title']
            news.description = request.POST['description']
            news.save()
        return render(request, 'app_news/change_news.html', context={'button_name': 'Обновить',
                                                                     'title': 'Редактировать новость',
                                                                     'news_form': news_form})

class NewsCreateView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/change_news.html', context={'button_name': 'Создать',
                                                                     'title': 'Создать новость',
                                                                     'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            News.objects.create(title=request.POST['title'],
                                description=request.POST['description'])
            return HttpResponseRedirect('/all-news')
        else:
            return render(request, 'app_news/change_news.html', context={'button_name': 'Создать',
                                                                         'title': 'Создать новость',
                                                                         'news_form': news_form})



class CommentsListView(View):

    def get(self, request, news_id):
        comments = Comment.objects.all().filter(news=self.request.resolver_match.kwargs['news_id']).order_by('create_date')
        comment_form = CommentForm()
        return render(request, 'app_news/show_comments.html', context={'comments': comments,
                                                                       'comment_form': comment_form})

    def post(self, request, news_id):

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(user_name=request.POST['user_name'],
                                   description=request.POST['description'],
                                   news=News.objects.get(id=news_id))
        comments = Comment.objects.all().filter(news=news_id).order_by('create_date')
        comment_form = CommentForm()
        return render(request, 'app_news/show_comments.html', context={'comments': comments,
                                                                       'comment_form': comment_form})
