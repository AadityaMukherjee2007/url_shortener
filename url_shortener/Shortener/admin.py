from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("slug", "original_url", "clicks", "created_at")
    search_fields = ("slug", "original_url")
