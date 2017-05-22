from django.contrib import admin
from .models import Category, Dll, API


class APIAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'dll', 'hash_value')
    search_fields = ('hash', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class DllAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(API, APIAdmin)
admin.site.register(Dll, DllAdmin)
admin.site.register(Category, CategoryAdmin)
