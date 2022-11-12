from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import AuthForm, UserRegisterForm, AddBalanceForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Storage
from typing import Union, List, Dict
# Create your views here.


def get_user_profile(user: User) -> Union[UserProfile, None]:
    try:
        user_profile = UserProfile.objects.get(user=user)
        return user_profile
    except UserProfile.DoesNotExist:
        return None


class BalancePage(View):

    def get(self, request):
        user = request.user
        if not user.is_anonymous:
            user_profile = get_user_profile(user)
            form = None
            if user_profile is not None:
                form = AddBalanceForm()
            return render(request,
                          'marketplace_cite/add_balance_page.html',
                          context={'form': form,
                                   'profile': user_profile,
                                   'is_exist': user_profile is not None})
        else:
            return HttpResponseRedirect('products-list')

    def post(self, request):
        user = request.user
        if not user.is_anonymous:
            user_profile = get_user_profile(user)
            balance_form = AddBalanceForm(request.POST)
            if balance_form.is_valid():
                balance = balance_form.cleaned_data['balance']
                if user_profile is not None:
                    user_profile.balance += balance
                    user_profile.save()

            return render(request,
                          'marketplace_cite/add_balance_page.html',
                          context={'form': balance_form,
                                   'profile': user_profile,
                                   'is_exist': user_profile is not None})
        else:
            return HttpResponseRedirect('products-list')


class PersonalCabinetView(View):

    def get(self, request):
        user = request.user

        if not user.is_anonymous:
            user_profile = get_user_profile(user)
            return render(request,
                          'marketplace_cite/personal_cabinet_page.html',
                          context={'profile': user_profile,
                                   'is_exist': user_profile is not None})
        else:
            return HttpResponseRedirect('products-list')


class PopularProductsView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/popular_products_page.html', context={})


class ProductsListView(View):

    def restructure_data(self, storages: List[Storage]) -> Dict[str, List[Storage]]:
        result = {}

        while len(storages) > 0:
            storage = storages.pop(0)
            current_product_name = storage.product.name
            if current_product_name not in result:
                result[current_product_name] = []
            result[current_product_name].append(storage)
        return result

    def get(self, request):
        storages = list(Storage.objects.select_related('shop').select_related('product').all())
        result = self.restructure_data(storages)
        user = request.user
        user_profile = None
        if not user.is_anonymous:
            user_profile = get_user_profile(user)
        return render(request, 'marketplace_cite/products_list_page.html', context={'data': result,
                                                                                    'show_button': user_profile is not None})


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