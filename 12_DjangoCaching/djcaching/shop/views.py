from django.shortcuts import render
from django.views.generic import TemplateView


class ShopsListView(TemplateView):
    template_name = 'shop/shops_list.html'


class UserPageView(TemplateView):
    template_name = 'shop/user_page.html'


class RegistartionView(TemplateView):
    template_name = 'shop/registration.html'


class ShopProductsView(TemplateView):
    template_name = 'shop/shop_products.html'


class ProductDetailsView(TemplateView):
    template_name = 'shop/product_details.html'
