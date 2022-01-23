from django.contrib import admin
from .models import ConfigAlert, Alert
# Register your models here.

class ConfigAlertAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(ConfigAlert, ConfigAlertAdmin)

class AlertAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Alert, AlertAdmin)
