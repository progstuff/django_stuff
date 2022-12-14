from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import AuthForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from .models import Shop, Discount, ProductInShop, Purchase, UserProfile
from django.core.cache import cache


class ShopsListView(View):

    def get(self, request, *args, **kwargs):
        shops_list = Shop.objects.all()
        return render(request, 'shop/page_shops_list.html', context={'shops': shops_list})


class UserPageView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_anonymous:
            discounts_cache_key = 'discounts:{}'.format(user.username)
            personal_offer_cache_key = 'personal_offer:{}'.format(user.username)
            purchases_cache_key = 'purchases:{}'.format(user.username)

            discounts = cache.get(discounts_cache_key)
            purchases = cache.get(purchases_cache_key)
            personal_offer = cache.get(personal_offer_cache_key)

            if (discounts is None) or (purchases is None) or (personal_offer is None):
                print('кэш пустой')
                discounts = Discount.objects.all()
                purchases = Purchase.objects.filter(user=user)
                personal_offer = ProductInShop.objects.order_by('?').first()

                user_cache_data = {
                    discounts_cache_key: discounts,
                    purchases_cache_key: purchases,
                    personal_offer_cache_key: personal_offer
                }
                cache.set_many(user_cache_data, 60)

            try:
                user_profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user, balance=0.0)

            return render(request, 'shop/page_user.html', context={'discounts': discounts,
                                                                   'purchases': purchases,
                                                                   'personal_offer': personal_offer,
                                                                   'user_profile': user_profile})
        else:
            return HttpResponseRedirect('shops-list')


class RegistartionView(View):

    def get(self, request, *args, **kwargs):
        register_form = UserRegisterForm()
        return render(request, 'shop/page_registration.html', context={'form': register_form})

    def post(self, request):
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect('shops-list')
        else:
            errors = register_form.errors
            register_form = UserRegisterForm()

            return render(request, 'shop/page_registration.html', context={'form': register_form, 'errors': errors.__str__()})


class ShopProductsView(View):

    def get(self, request, shop_id):
        shop = Shop.objects.get(id=shop_id)
        products_list = ProductInShop.objects.filter(shop=shop)

        return render(request, 'shop/page_shop_products.html', context={'products': products_list,
                                                                        'shop': shop,
                                                                        })


class ProductDetailsView(View):

    def get(self, request, product_in_shop_id):
        product_in_shop = ProductInShop.objects.get(id=product_in_shop_id)
        return render(request, 'shop/page_product_details.html', context={'product_in_shop': product_in_shop})


class LogOutView(LogoutView):
    template_name = "shop/page_logout.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_anonymous:
            logout(request)
        else:
            return HttpResponseRedirect('shops-list')


class LoginView(View):

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

