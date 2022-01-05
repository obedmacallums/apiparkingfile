from django.contrib import admin
from .models import ConfigAlert
# Register your models here.

class ConfigAlertAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(ConfigAlert, ConfigAlertAdmin)
