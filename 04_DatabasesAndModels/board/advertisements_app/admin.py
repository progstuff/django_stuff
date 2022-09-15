from django.contrib import admin
from advertisements_app.models import Advertisement, AdvertisementCategory, Author


@admin.register(Advertisement)
class AdvertisementsAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementCategory)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register your models here.