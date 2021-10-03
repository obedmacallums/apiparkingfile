from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Domain

admin.site.register(User, UserAdmin)


class DomainAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Domain, DomainAdmin)
