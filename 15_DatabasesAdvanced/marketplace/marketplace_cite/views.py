from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import AuthForm, UserRegisterForm, AddBalanceForm, PeriodForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Storage, BasketItem, Purchase
from typing import Union, List, Dict
from django.db.models import Sum, F
from django.db.models.query import QuerySet
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# Create your views here.


def get_user_profile(user: User) -> Union[UserProfile, None]:
    try:
        user_profile = UserProfile.objects.get(user=user)
        return user_profile
    except UserProfile.DoesNotExist:
        return None


def calculate_total_sum(data: QuerySet[BasketItem]) -> float:
    data = data.annotate(sub_total=F('price') * F('count'))
    total_sum = data.aggregate(Sum('sub_total'))
    total_sum = total_sum['sub_total__sum']
    if total_sum is None:
        total_sum = 0
    return total_sum, data


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
                    logger.info('???????????? ????????????????')

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
            data = []
            if user_profile is not None:

                data = Purchase.objects.filter(user=user_profile)\
                    .select_related('shop')\
                    .select_related('product')\
                    .order_by('-create_date')\
                    .annotate(sub_total=F('price') * F('count')).all()

                total_sum = data.aggregate(Sum('sub_total'))
                total_sum = total_sum['sub_total__sum']
                if total_sum is None:
                    total_sum = 0

                data = list(data)

            return render(request,
                          'marketplace_cite/personal_cabinet_page.html',
                          context={'profile': user_profile,
                                   'is_exist': user_profile is not None,
                                   'purchases': data,
                                   'total_sum': total_sum})
        else:
            return HttpResponseRedirect('products-list')


class PopularProductsView(View):

    def monthdelta(self, date: datetime, delta: int) -> datetime:
        m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12
        if not m: m = 12
        d = min(date.day, [31,
                           29 if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0) else 28,
                           31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
        return date.replace(day=d, month=m, year=y)

    def get(self, request):
        form = PeriodForm()
        ## ?????????????????????? ???? id ????????????
        min_date = self.monthdelta(datetime.now(), -1)
        result = list(Purchase.objects.filter(create_date__gt=min_date)
                      .values('product__id', 'product__name')
                      .annotate(total_cnt=Sum('count'))
                      .order_by('-total_cnt')
                      )
        ###########################
        return render(request, 'marketplace_cite/popular_products_page.html', context={'data': result,
                                                                                       'form': form})

    def post(self, request):
        form = PeriodForm(request.POST)

        period = int(form.data['period'])
        if period == 0:
            ## ?????????????????????? ???? id ????????????
            result = list(Purchase.objects
                          .values('product__id', 'product__name')
                          .annotate(total_cnt=Sum('count'))
                          .order_by('-total_cnt')
                          )
            ###########################
        else:
            min_date = self.monthdelta(datetime.now(), -period)
            ## ?????????????????????? ???? id ????????????
            result = list(Purchase.objects.filter(create_date__gt=min_date)
                          .values('product__id', 'product__name')
                          .annotate(total_cnt=Sum('count'))
                          .order_by('-total_cnt')
                          )
            ###########################

        return render(request, 'marketplace_cite/popular_products_page.html', context={'data': result,
                                                                                       'form': form})

class ProductsListView(View):

    def restructure_data(self, storages: List[Storage]) -> Dict[str, List[Storage]]:
        result = {}

        while len(storages) > 0:
            storage = storages.pop(0)
            current_product_name = storage.product.name
            if current_product_name not in result:
                result[current_product_name] = []
            result[current_product_name].append(storage)

        i = 0
        short_result = {}
        for key in result:
            short_result[key] = result[key]
            i += 1
            if i > 100:
                break
        return short_result

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
                    storage = Storage.objects.get(id=storage_id)
                    try:
                        basket = BasketItem.objects.get(user=user_profile, storage__id=storage_id)
                        if storage.count > basket.count:
                            basket.count += 1
                            basket.price = basket.storage.price
                            basket.save()

                    except BasketItem.DoesNotExist:
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
                ######################## ?????????????? ?????????? ??????????????
                total_sum, data = calculate_total_sum(data)
                ##############################################

            return render(request, 'marketplace_cite/purchase_page.html',
                          context={'total_sum': total_sum,
                                   'show_data': user_profile is not None,
                                   'user_profile': user_profile,
                                   'need_add_balance': total_sum > user_profile.balance})

        return HttpResponseRedirect('products-list')

    def post(self, request):
        user = request.user
        if not user.is_anonymous:
            user_profile = get_user_profile(user)
            if user_profile is not None:

                ################ ???????????????????? ?????????????? ???? ??????????????
                data = BasketItem.objects.filter(user=user_profile)\
                    .select_related('storage')\
                    .select_related('storage__product')\
                    .select_related('storage__shop')
                ##############################################

                ######################## ?????????????? ?????????? ??????????????
                total_sum, data = calculate_total_sum(data)
                ##############################################

                ############# ???????????????? ?????????????? ???????????? ???? ????????????
                is_overflow = False
                for item in data:
                    if item.count > item.storage.count:
                        is_overflow = True
                        break
                ##############################################

                if not is_overflow:

                    ################## ???????????????? ?????????????? ?? ??????????????
                    for item in data:
                        Purchase.objects.create(shop=item.storage.shop,
                                                product=item.storage.product,
                                                price=item.price,
                                                count=item.count,
                                                user=user_profile)
                    ##############################################

                    ##### ???????????????????? ???????????????????? ???? ????????????
                    for item in data:
                        item.storage.count -= item.count
                        item.storage.save()
                    #####################################

                    data.delete()# ???????????????? ?????????????? ?? ??????????????

                    data = Purchase.objects.filter(user=user_profile) \
                        .annotate(sub_total=F('price') * F('count')).all()

                    total_purchase_sum = data.aggregate(Sum('sub_total'))
                    total_purchase_sum = total_purchase_sum['sub_total__sum']
                    if total_purchase_sum is None:
                        total_purchase_sum = 0

                    if (total_purchase_sum > 20000) and (total_purchase_sum <= 30000):
                        user_status = 'C'
                    elif total_purchase_sum > 30000:
                        user_status = '??'
                    else:
                        user_status = '??'

                    prev_status = user_profile.status
                    if prev_status != user_status:
                        logger.info('???????????? ???????????????????????? ??????????????')

                    ################## ???????????????????? ??????????????
                    user_profile.balance -= total_sum
                    user_profile.status = user_status
                    user_profile.save()
                    #####################################
                    logger.info('?????????? ?????????????? ?? ??????????????')
                    logger.info('?????????? ????????????????')

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

                ######################## ?????????????? ?????????? ??????????????
                total_sum, data = calculate_total_sum(data)
                ##############################################

                basket_items = list(data.all())
                is_not_overflow = True
                for basket_item in basket_items:
                    if basket_item.count > basket_item.storage.count:
                        is_not_overflow = False
            return render(request, 'marketplace_cite/shopping_cart_page.html',
                          context={'basket_items': basket_items,
                                   'total_sum': total_sum,
                                   'show_data': user_profile is not None,
                                   'is_not_overflow': is_not_overflow})
        return HttpResponseRedirect('products-list')

    def post(self, request):
        user = request.user
        if not user.is_anonymous:
            user_profile = get_user_profile(user)
            basket_items = []
            total_sum = 0
            if user_profile is not None:

                data = BasketItem.objects.filter(user=user_profile)
                data.delete()  # ???????????????? ?????????????? ?? ??????????????

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
                    logger.info('???????????????????????? ????????????????????????????????')
                    return HttpResponseRedirect('/products-list')
                else:
                    auth_form.add_error('__all__', '?????????????? ???????????? ???? ??????????????')
            else:
                auth_form.add_error('__all__', '???????????? ?? ???????????? ?????? ????????????')
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