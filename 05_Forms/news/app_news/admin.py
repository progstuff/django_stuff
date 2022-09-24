from django.contrib import admin
from .models import News, Comment, User

class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    actions = ['set_active', 'set_not_active']
    list_display = ['title', 'create_date', 'update_date', 'is_active']
    list_filter = ['is_active']
    inlines = [CommentInline]

    def set_active(self, request, queryset):
        queryset.update(is_active=True)

    def set_not_active(self, request, queryset):
        queryset.update(is_active=False)

    set_active.short_description = 'сделать активной'
    set_not_active.short_description = 'сделать не активной'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ['mark_as_published', 'mark_as_deleted']
    list_display = ['user', 'create_date', 'update_date', 'news', 'short_description', 'status']
    list_filter = ['user']

    def mark_as_published(self, request, queryset):
        queryset.update(status='p')

    def mark_as_deleted(self, request, queryset):
        queryset.update(status='d')

    mark_as_published.short_description = 'опубликовать'
    mark_as_deleted.short_description = 'удалено администратором'


