from django.contrib import admin
from .models import Dll, API, MalwareAPICall


class APIAdmin(admin.ModelAdmin):
    list_display = ('name', 'hash_value')
    search_fields = ('name',)


class DllAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class MalwareAPICallAdmin(admin.ModelAdmin):
    list_display = ('sha256', 'api', 'dll', 'count')
    search_fields = ('sha256', )

admin.site.register(API, APIAdmin)
admin.site.register(Dll, DllAdmin)
admin.site.register(MalwareAPICall, MalwareAPICallAdmin)
