from django.urls import path
from . import views


urlpatterns = [
    path('add-balance', views.BalancePage.as_view(), name='balance'),
    path('login', views.AuthenticationView.as_view(), name='login'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('personal-cabinet', views.PersonalCabinetView.as_view(), name='personal-cabinet'),
    path('popular-products', views.PopularProductsView.as_view(), name='popular-products'),
    path('products-list', views.ProductsListView.as_view(), name='products-list'),
    path('purchase', views.PurchaseView.as_view(), name='purchase'),
    path('registration', views.RegistrationView.as_view(), name='registration'),
    path('shopping-cart', views.ShoppingCartView.as_view(), name='shopping-cart'),
]