from django.urls import path
from . import views

urlpatterns = [
    path('shops-list', views.ShopsListView.as_view(), name='shops-list'),
    path('login', views.LoginView.as_view(), name='login'),
    path('user-page', views.UserPageView.as_view(), name='user-page'),
    path('registration', views.RegistartionView.as_view(), name='registration'),
    path('shop-products', views.ShopProductsView.as_view(), name='shop-products'),
    path('product-details', views.ProductDetailsView.as_view(), name='product-details'),
]