from django.contrib import admin
from .models import UserProfile, Shop, Product, Purchase, Storage


@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'balance', 'status', 'user']


@admin.register(Shop)
class ShopModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Purchase)
class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'product', 'user', 'count', 'price']


@admin.register(Storage)
class StorageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'product', 'count', 'price']