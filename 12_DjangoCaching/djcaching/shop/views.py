from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import AuthForm
from django.contrib.auth import authenticate, login
#from django.contrib.auth.views import LogoutView


class ShopsListView(TemplateView):
    template_name = 'shop/page_shops_list.html'


class UserPageView(TemplateView):
    template_name = 'shop/page_user.html'


class RegistartionView(TemplateView):
    template_name = 'shop/page_registration.html'


class ShopProductsView(TemplateView):
    template_name = 'shop/page_shop_products.html'


class ProductDetailsView(TemplateView):
    template_name = 'shop/page_product_details.html'


class LoginView(TemplateView):
    template_name = "shop/page_login.html"

    def post(self, request, *args, **kwargs):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/shops-list')
                else:
                    auth_form.add_error('__all__', 'Учётная запись не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка в логине или пароле')
        return render(request, 'shop/page_login.html', context={'form': auth_form})

    def get(self, request, *args, **kwargs):
        auth_form = AuthForm()
        return render(request, 'shop/page_login.html', context={'form': auth_form})