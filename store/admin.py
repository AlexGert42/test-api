from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Book


# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
    # prepopulated_fields = {"slug": ("title",)}




@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass

# admin.site.register(Book, TodoAdmin)
