from django.shortcuts import render
from django.views.generic import TemplateView


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

