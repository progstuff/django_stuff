from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import AuthForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
# Create your views here.


class BalancePage(View):

    def get(self, request):
        return render(request, 'marketplace_cite/add_balance_page.html', context={})


class PersonalCabinetView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/personal_cabinet_page.html', context={})


class PopularProductsView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/popular_products_page.html', context={})


class ProductsListView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/products_list_page.html', context={})


class PurchaseView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/purchase_page.html', context={})


class ShoppingCartView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/shopping_cart_page.html', context={})


class LogOutView(View):
    
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_anonymous:
            logout(request)
            return render(request, 'marketplace_cite/logout_page.html', context={})
        else:
            return HttpResponseRedirect('products-list')


class AuthenticationView(View):

    def post(self, request, *args, **kwargs):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/products-list')
                else:
                    auth_form.add_error('__all__', 'Учётная запись не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка в логине или пароле')
        return render(request, 'marketplace_cite/authentication_page.html', context={'form': auth_form})

    def get(self, request, *args, **kwargs):
        auth_form = AuthForm()
        return render(request, 'marketplace_cite/authentication_page.html', context={'form': auth_form})


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        register_form = UserRegisterForm()
        return render(request, 'marketplace_cite/registration_page.html', context={'form': register_form})

    def post(self, request):
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('products-list')
        else:
            errors = register_form.errors
            register_form = UserRegisterForm()

            return render(request, 'marketplace_cite/registration_page.html', context={'form': register_form, 'errors': errors.__str__()})