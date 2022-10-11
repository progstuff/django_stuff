from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from .forms import UserRegisterForm, AuthForm
from django.contrib.auth import authenticate, login
from .models import Record


class AllPosts(TemplateView):
    template_name = 'files_test/all_posts.html'

    def get(self, request, *args, **kwargs):
        all_posts = Record.objects.all()
        return render(request, 'files_test/all_posts.html', context={'posts': all_posts})


class PostDetails(TemplateView):
    template_name = 'files_test/post_details.html'

    def get(self, request, post_id):
        post = Record.objects.get(id=post_id)
        return render(request, 'files_test/post_details.html', context={'post': post})


class UserPage(TemplateView):
    template_name = 'files_test/user_page.html'


class PostCreate(TemplateView):
    template_name = 'files_test/post_create.html'


class LogInView(TemplateView):
    template_name = "files_test/login_page.html"

    def post(self, request, *args, **kwargs):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/all-posts')
                else:
                    auth_form.add_error('__all__', 'Учётная запись не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка в логине или пароле')
        return render(request, 'files_test/login_page.html', context={'form': auth_form})

    def get(self, request, *args, **kwargs):
        auth_form = AuthForm()
        return render(request, 'files_test/login_page.html', context={'form': auth_form})


class RegisterPage(View):

    def get(self, request, *args, **kwargs):
        register_form = UserRegisterForm()
        return render(request, 'files_test/register_page.html', context={'form': register_form})

    def post(self, request):
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('all-posts')
        else:
            errors = register_form.errors
            register_form = UserRegisterForm()

            return render(request, 'files_test/register_page.html', context={'form': register_form, 'errors': errors.__str__()})
