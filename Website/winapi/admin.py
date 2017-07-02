from django.contrib import admin
from .models import Dll, API, MalwareAPICall, MalwareAPICallExcutionTrace


class APIAdmin(admin.ModelAdmin):
    list_display = ('name', 'hash_value')
    search_fields = ('name',)


class DllAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class MalwareAPICallExcutionTracelAdmin(admin.ModelAdmin):
    list_display = ('sha256', )
    search_fields = ('sha256', )


class MalwareAPICallAdmin(admin.ModelAdmin):
    list_display = ('malware_excution_trace', 'api', 'dll', 'count')
    search_fields = ('malware_excution_trace__sha256', )

admin.site.register(API, APIAdmin)
admin.site.register(Dll, DllAdmin)
admin.site.register(MalwareAPICallExcutionTrace, MalwareAPICallExcutionTracelAdmin)
admin.site.register(MalwareAPICall, MalwareAPICallAdmin)
