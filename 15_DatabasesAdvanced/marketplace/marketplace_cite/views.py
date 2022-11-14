from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import AuthForm, UserRegisterForm, AddBalanceForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Storage, BasketItem
from typing import Union, List, Dict
from django.db.models import Sum
from django.db.models import F
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
        storages = list(Storage.objects.select_related('shop').select_related('product').order_by('price').all())
        result = self.restructure_data(storages)
        user = request.user
        user_profile = None
        count_items = 0
        total_sum = 0
        if not user.is_anonymous:
            user_profile = get_user_profile(user)
            if user_profile is not None:
                count_items = self.calculate_products_in_basket(user_profile)
                total_sum = self.calculate_total_sum_in_basket(user_profile)
        return render(request,
                      'marketplace_cite/products_list_page.html',
                      context={'data': result,
                               'show_button': user_profile is not None,
                               'basket_items_cnt': count_items,
                               'total_sum': total_sum})

    def post(self, request):
        user = request.user
        if not user.is_anonymous:
            storages = list(Storage.objects.select_related('shop').select_related('product').order_by('price').all())
            result = self.restructure_data(storages)
            user_profile = get_user_profile(user)
            count_items = 0
            total_sum = 0
            if user_profile is not None:
                try:
                    storage_id = int(request.POST['add_button'])
                    try:
                        basket = BasketItem.objects.get(user=user_profile, storage__id=storage_id)
                        basket.count += 1
                        basket.price = basket.storage.price
                        basket.save()
                    except BasketItem.DoesNotExist:
                        storage = Storage.objects.get(id=storage_id)
                        BasketItem.objects.create(user=user_profile,
                                                  storage=storage,
                                                  count=1,
                                                  price=storage.price)

                    count_items = self.calculate_products_in_basket(user_profile)
                    total_sum = self.calculate_total_sum_in_basket(user_profile)
                except ValueError:
                    pass
            return render(request,
                          'marketplace_cite/products_list_page.html',
                          context={'data': result,
                                   'show_button': user_profile is not None,
                                   'basket_items_cnt': count_items,
                                   'total_sum': total_sum})
        else:
            return HttpResponseRedirect('products-list')

    def calculate_products_in_basket(self, user_profile: UserProfile) -> int:
        count_items = BasketItem.objects.filter(user=user_profile).aggregate(Sum('count'))
        count_items = count_items['count__sum']
        if count_items is None:
            count_items = 0
        return count_items

    def calculate_total_sum_in_basket(self, user_profile: UserProfile) -> float:
        total_sum = BasketItem.objects.filter(user=user_profile).annotate(sub_total=F('price') * F('count'))
        total_sum = total_sum.aggregate(Sum('sub_total'))
        total_sum = total_sum['sub_total__sum']
        if total_sum is None:
            return 0
        return total_sum


class PurchaseView(View):

    def get(self, request):
        user = request.user
        if not user.is_anonymous:

            user_profile = get_user_profile(user)
            total_sum = 0
            if user_profile is not None:
                data = BasketItem.objects.filter(user=user_profile).select_related('storage')
                data = data.annotate(sub_total=F('price') * F('count'))
                total_sum = data.aggregate(Sum('sub_total'))
                total_sum = total_sum['sub_total__sum']
                if total_sum is None:
                    total_sum = 0
            return render(request, 'marketplace_cite/purchase_page.html',
                          context={'total_sum': total_sum,
                                   'show_data': user_profile is not None,
                                   'user_profile': user_profile,
                                   'need_add_balance': total_sum > user_profile.balance})

        return HttpResponseRedirect('products-list')


class ShoppingCartView(View):

    def get(self, request):
        user = request.user
        if not user.is_anonymous:
            user_profile = get_user_profile(user)
            basket_items = []
            total_sum = 0
            if user_profile is not None:
                data = BasketItem.objects.filter(user=user_profile).select_related('storage')
                data = data.annotate(sub_total=F('price') * F('count'))
                total_sum = data.aggregate(Sum('sub_total'))
                total_sum = total_sum['sub_total__sum']
                if total_sum is None:
                    total_sum = 0

                basket_items = list(data.all())
            return render(request, 'marketplace_cite/shopping_cart_page.html',
                          context={'basket_items': basket_items,
                                   'total_sum': total_sum,
                                   'show_data': user_profile is not None})
        return HttpResponseRedirect('products-list')


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