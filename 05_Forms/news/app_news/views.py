
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Comment
from .forms import NewsForm, CommentForm
from django.views import generic, View


class NewsListView(generic.ListView):
    model = News
    template_name = 'app_news/show_news.html'
    context_object_name = 'all_news'
    queryset = News.objects.all()


class NewsDetailView(View):

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/change_news.html', context={'news_id': news_id,
                                                                     'news_form': news_form})


class CommentsListView(View):

    def get(self, request, news_id):
        comments = Comment.objects.all().filter(news=self.request.resolver_match.kwargs['news_id'])
        comment_form = CommentForm()
        return render(request, 'app_news/show_comments.html', context={'comments': comments,
                                                                       'comment_form': comment_form})

    def post(self, request, news_id):

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(user_name=request.POST['user_name'],
                                   description=request.POST['description'],
                                   news=News.objects.get(id=news_id))
        comments = Comment.objects.all().filter(news=news_id)
        comment_form = CommentForm()
        return render(request, 'app_news/show_comments.html', context={'comments': comments,
                                                                       'comment_form': comment_form})
