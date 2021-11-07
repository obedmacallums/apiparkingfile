from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Domain, Agent, Camera, Category, MetaData, AddedInfo, Entry
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


admin.site.register(User, UserAdmin)


class DomainAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Domain, DomainAdmin)


class AgentAdmin(admin.ModelAdmin):
     formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Agent, AgentAdmin)


class CameraAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Camera, CameraAdmin)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Category, CategoryAdmin)

class MetaDataAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(MetaData, MetaDataAdmin)


class AddedInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(AddedInfo, AddedInfoAdmin)

class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Entry, EntryAdmin)

