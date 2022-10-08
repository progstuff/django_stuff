from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from .forms import UserRegisterForm


class AllPosts(TemplateView):
    template_name = 'files_test/all_posts.html'


class PostDetails(TemplateView):
    template_name = 'files_test/post_details.html'


class UserPage(TemplateView):
    template_name = 'files_test/user_page.html'


class PostCreate(TemplateView):
    template_name = 'files_test/post_create.html'


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
