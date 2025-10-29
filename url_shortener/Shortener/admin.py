from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("slug", "original_url", "clicks", "created_at")
    search_fields = ("slug", "original_url")
    readonly_fields = ("clicks", "last_accessed", "created_at")
    ordering = ("-created_at",)
    list_filter = ("created_at",)
    fieldsets = (
        (None, {
            'fields': ('original_url', 'slug')
        }),
        ('Statistics', {
            'fields': ('clicks', 'last_accessed', 'created_at')
        }),
    )

    def has_add_permission(self, request):
        return True
    

    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    def has_view_permission(self, request, obj=None):
        return True
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


    def delete_model(self, request, obj):
        super().delete_model(request, obj)
    def get_queryset(self, request):
        return super().get_queryset(request)
    


    