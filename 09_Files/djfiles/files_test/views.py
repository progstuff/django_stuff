from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from .forms import UserRegisterForm, AuthForm, UserPageForm, RecordForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .models import UserProfile, RecordFiles, Record


class AllPosts(TemplateView):
    template_name = 'files_test/all_posts.html'

    def get(self, request, *args, **kwargs):
        all_posts = Record.objects.all().order_by('-create_date')
        return render(request, 'files_test/all_posts.html', context={'posts': all_posts})

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect('create-post')


class PostDetails(TemplateView):
    template_name = 'files_test/post_details.html'

    def get(self, request, post_id):
        post = Record.objects.get(id=post_id)
        return render(request, 'files_test/post_details.html', context={'post': post})


class UserPage(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_anonymous:
            try:
                user_profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user, first_name='', last_name='', about='')
            user_form = UserPageForm(instance=user_profile)
            return render(request, 'files_test/user_page.html', context={'form': user_form})
        else:
            return HttpResponseRedirect('all-posts')

    def post(self, request):
        user = request.user
        if not user.is_anonymous:
            try:
                user_profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user, first_name='', last_name='', about='')

            user_form = UserPageForm(request.POST, instance=user_profile)
            if user_form.is_valid():
                user_form.save()
                return HttpResponseRedirect('all-posts')
            else:
                errors = user_form.errors

                user_form = UserPageForm(instance=user_profile)

                return render(request, 'files_test/user_page.html', context={'form': user_form, 'errors': errors.__str__()})
        else:
            return HttpResponseRedirect('all-posts')


class PostCreate(TemplateView):
    template_name = 'files_test/post_create.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_anonymous:
            record_form = RecordForm()
            return render(request, 'files_test/post_create.html', context={'form': record_form})
        else:
            return HttpResponseRedirect('all-posts')

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_anonymous:
            record_form = RecordForm(request.POST, request.FILES)
            if record_form.is_valid():
                title = record_form.cleaned_data['title']
                description = record_form.cleaned_data['description']
                record = Record.objects.create(user=user, title=title, description=description)
                files = request.FILES.getlist('file')
                for file in files:
                    RecordFiles.objects.create(record=record, file=file)
                return HttpResponseRedirect('all-posts')
            else:
                return render(request, 'files_test/post_create.html', context={'form': record_form})
        else:
            return HttpResponseRedirect('all-posts')


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


class LogOutView(LogoutView):
    template_name = "files_test/logout.html"


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
