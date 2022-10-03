
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Comment, UserProfile
from .forms import NewsForm, AuthForm, get_comment_form, ExtendedUserRegisterForm
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User, Permission
from django.db.models import Q


class UserPage(TemplateView):
    template_name = 'app_news/user_page.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        data = UserProfile.objects.all()
        users = {}
        news = {}
        permissions = Permission.objects.filter(user=request.user)
        moderator_permission = Permission.objects.get(codename='moderator')
        veruser_permission = Permission.objects.get(codename='verificateduser')
        if user.has_perm('app_news.moderator_userprofile') or moderator_permission in permissions:
            users = UserProfile.objects.filter(Q(user_request=1) | Q(user_request=2))
            try:
                user_profile = data.get(user=user)
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user, phone="-", town='-', user_state=2)
            news = News.objects.filter(is_active=False).order_by('-create_date')
        elif veruser_permission in permissions:
            user_profile = data.get(user=user)
            news = News.objects.filter(Q(is_active=False) & Q(user=user)).order_by('-create_date')
        else:
            user_profile = data.get(user=user)

        return render(request, 'app_news/user_page.html', context={'user_profile': user_profile,
                                                                   'users': users,
                                                                   'news': news})

    def post(self, request, *args, **kwargs):
        user = request.user
        data = UserProfile.objects.all()
        users = {}
        news = {}

        permissions = Permission.objects.filter(user=request.user)
        moderator_permission = Permission.objects.get(codename='moderator')
        veruser_permission = Permission.objects.get(codename='verificateduser')
        if user.has_perm('app_news.moderator_userprofile') or moderator_permission in permissions:
            req_data = request.POST.get('data', None)

            if req_data is not None:
                req_data = req_data.split(':')
                usr = User.objects.get(username=req_data[0])
                usr_profile = data.get(user=usr)
                if req_data[2] == 'ok':
                    if req_data[1] == 'ver':
                        usr_profile.user_state = 1
                        permission = Permission.objects.get(codename='verificateduser')
                        usr.user_permissions.add(permission)

                    elif req_data[1] == 'mod':
                        usr_profile.user_state = 2
                        permission = Permission.objects.get(codename='moderator')
                        usr.user_permissions.add(permission)
                usr_profile.user_request = 0
                usr_profile.save()
            elif request.POST.get('n_data', None) is not None:
                nws = News.objects.get(id=request.POST['n_data'])
                nws.is_active = True
                nws.save()
            elif request.POST.get('n_data_no', None) is not None:
                nws = News.objects.get(id=request.POST['n_data_no'])
                profile = UserProfile.objects.get(user=nws.user)
                profile.news_cnt = News.objects.filter(user=nws.user).count() - 1
                profile.save()
                News.objects.filter(id=request.POST['n_data_no']).delete()
            else:
                req_data = request.POST['data_no'].split(':')
                usr = User.objects.get(username=req_data[0])
                usr_profile = data.get(user=usr)

                usr_profile.user_request = 0
                usr_profile.save()

            users = UserProfile.objects.filter(Q(user_request=1) | Q(user_request=2))
            data = UserProfile.objects.all()
            try:
                user_profile = data.get(user=user)
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user, phone="-", town='-', user_state=2)
            news = News.objects.filter(is_active=False).order_by('-create_date')
        else:
            user_profile = data.get(user=user)
            if request.POST['data'] == 'moderator_request':
                user_profile.user_request = 2
                user_profile.save()
            elif request.POST['data'] == 'verified_request':
                user_profile.user_request = 1
                user_profile.save()

            if veruser_permission in permissions:
                news = News.objects.filter(Q(is_active=False) & Q(user=user)).order_by('-create_date')

        return render(request, 'app_news/user_page.html', context={'user_profile': user_profile,
                                                                   'users': users,
                                                                   'news': news})

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
        news = News.objects.filter(is_active=True).order_by('tag', '-create_date')
        user = request.user
        is_has_perm = False
        if not user.is_anonymous:
            permissions = Permission.objects.filter(user=request.user)
            permission = Permission.objects.get(codename='verificateduser')
            is_has_perm = user.has_perm('app_news.verificateduser_userprofile') or (permission in permissions)
        return render(request, 'app_news/show_news.html', context={'all_news': news,
                                                                   'username': user.username,
                                                                   'is_has_perm': is_has_perm})

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
            news.is_active = False
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
            user = request.user
            News.objects.create(user=request.user,
                                title=request.POST['title'],
                                description=request.POST['description'],
                                is_active=False)
            profile = UserProfile.objects.get(user=user)
            profile.news_cnt = News.objects.filter(user=user).count()
            profile.save()
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
                user = User.objects.get(username=user_name)

            except User.DoesNotExist:
                user = User.objects.create(username=user_name, password=user_name)

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
                    user_profile = UserProfile.objects.get(user=user)
                    add_permission(user, user_profile)
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


def add_permission(user, user_profile):
    if user_profile.user_state == 1:
        permission = Permission.objects.get(codename='verificateduser')
        user.user_permissions.add(permission)
        user.save()
    elif user_profile.user_state == 2:
        permission = Permission.objects.get(codename='moderator')
        user.user_permissions.add(permission)
        user.save()
