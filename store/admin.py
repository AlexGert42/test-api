from django.contrib import admin
from .models import Book


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book, TodoAdmin)
