from django.contrib import admin
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ('names',)

admin.site.register(Certificate, CertificateAdmin)