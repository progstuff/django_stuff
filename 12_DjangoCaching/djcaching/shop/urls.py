from django.urls import path
from . import views

urlpatterns = [
    path('shops-list', views.ShopsListView.as_view(), name='shops-list'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('user-page', views.UserPageView.as_view(), name='user-page'),
    path('registration', views.RegistartionView.as_view(), name='registration'),
    path('shop-products/<int:shop_id>', views.ShopProductsView.as_view(), name='shop-products'),
    path('product-details/<int:product_in_shop_id>', views.ProductDetailsView.as_view(), name='product-details'),
]