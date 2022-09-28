
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Comment, User
from .forms import NewsForm, AuthForm, get_comment_form, ExtendedUserRegisterForm
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        register_form = ExtendedUserRegisterForm()
        return render(request, 'app_news/register.html', context={'form': register_form})

    def post(self, request):
        register_form = ExtendedUserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('all-news')
        else:
            errors = register_form.errors
            register_form = ExtendedUserRegisterForm()
            return render(request, 'app_news/register.html', context={'form': register_form, 'errors': errors})


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
        comment_form = get_comment_form(request.user.is_authenticated)
        return render(request, 'app_news/show_comments.html', context={'comments': comments,
                                                                       'comment_form': comment_form})

    def post(self, request, news_id):

        comment_form = get_comment_form(request.user.is_authenticated, request.POST)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                user_name = request.user.username
            else:
                user_name = request.POST['user']

            try:
                user = User.objects.get(user_name=user_name)
            except User.DoesNotExist:
                user = User.objects.create(user_name=user_name)

            Comment.objects.create(user=user,
                                   description=request.POST['description'],
                                   news=News.objects.get(id=news_id),
                                   is_anonim=not request.user.is_authenticated)
        comments = Comment.objects.all().filter(news=news_id).order_by('-create_date')
        comment_form = get_comment_form(request.user.is_authenticated, request.POST)

        return render(request, 'app_news/show_comments.html', context={'comments': comments,
                                                                       'comment_form': comment_form})


class LogInView(TemplateView):
    template_name = "app_news/login.html"

    def post(self, request, *args, **kwargs):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/all-news')
                else:
                    auth_form.add_error('__all__', 'Учётная запись не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка в логине или пароле')
        return render(request, 'app_news/login.html', context={'form': auth_form})

    def get(self, request, *args, **kwargs):
        auth_form = AuthForm()
        return render(request, 'app_news/login.html', context={'form':auth_form})


class LogOutView(LogoutView):
    template_name = "app_news/logout.html"


