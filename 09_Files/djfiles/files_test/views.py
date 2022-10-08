from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class AllPosts(TemplateView):
    template_name = 'files_test/all_posts.html'


class PostDetails(TemplateView):
    template_name = 'files_test/post_details.html'


class UserPage(TemplateView):
    template_name = 'files_test/user_page.html'


class PostCreate(TemplateView):
    template_name = 'files_test/post_create.html'


class RegisterPage(TemplateView):
    template_name = 'files_test/register_page.html'
