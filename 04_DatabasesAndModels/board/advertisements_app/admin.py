from django.contrib import admin
from advertisements_app.models import Advertisement, AdvertisementCategory


@admin.register(Advertisement)
class AdvertisementsAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementCategory)
class CategoryAdmin(admin.ModelAdmin):
    pass

# Register your models here.