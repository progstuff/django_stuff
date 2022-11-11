from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class BalancePage(View):

    def get(self, request):
        return render(request, 'marketplace_cite/add_balance_page.html', context={})


class AuthenticationView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/authentication_page.html', context={})


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


class RegistrationView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/registration_page.html', context={})


class ShoppingCartView(View):

    def get(self, request):
        return render(request, 'marketplace_cite/shopping_cart_page.html', context={})