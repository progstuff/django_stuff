
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Comment
from .forms import NameForm
from django.views import generic


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'app_news/name.html', {'form': form})


class AdvertisementsListView(generic.ListView):
    model = News
    template_name = 'app_news/show_news.html'
    context_object_name = 'all_news'
    queryset = News.objects.all()


def show_all_news(request):
    return render(request, 'app_news/show_news.html', {})


def create_news(request):
    return render(request, 'app_news/create_news.html', {})


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'app_news/change_news.html'
    context_object_name = 'news'


class CommentsListView(generic.ListView):
    model = Comment
    template_name = 'app_news/show_comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        comments = Comment.objects.all().filter(news=self.request.resolver_match.kwargs['pk'])
        return comments
