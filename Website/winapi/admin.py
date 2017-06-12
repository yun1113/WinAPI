from django.contrib import admin
from .models import Dll, API


class APIAdmin(admin.ModelAdmin):
    list_display = ('name', 'hash_value')
    search_fields = ('name',)


class DllAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(API, APIAdmin)git
admin.site.register(Dll, DllAdmin)
