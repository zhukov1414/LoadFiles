from django.contrib import admin

from files.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'processed')
    list_filter = ('processed',)
    search_fields = ('file__name',)


admin.site.register(File, FileAdmin)
