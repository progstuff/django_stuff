from django.contrib import admin
from .models import Shop, Product, ProductInShop, Purchase, UserProfile, Discount
# Register your models here.


@admin.register(Shop)
class ShopModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'addres']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(ProductInShop)
class ProductInShopModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'shop', 'price', 'count']


@admin.register(Purchase)
class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'shop',
                    'bought_price', 'count', 'create_date']


@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'balance']


@admin.register(Discount)
class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']