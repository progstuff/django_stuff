from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'create_date', 'update_date']