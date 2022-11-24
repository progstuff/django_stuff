from django.contrib import admin
from .models import HouseType, Housing, RoomsNumber, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_date']


@admin.register(HouseType)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']


@admin.register(RoomsNumber)
class RoomsNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_type']


@admin.register(Housing)
class HousingAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'house_type', 'rooms_number']
