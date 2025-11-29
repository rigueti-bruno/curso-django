from django.contrib import admin
from .models import Tag

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id','nome','slug',
    list_display_links = 'id','slug',
    search_fields = 'id','slug','nome',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {'slug': ('nome',)}