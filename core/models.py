from django.db import models
from .custom import domain_validator, alphanumeric_upper_space, file_name_validator
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields
from django.core.validators import URLValidator
from .forms import LocalURLFormField



class LocalURLField(models.URLField):
    default_validators = [URLValidator(schemes=['rtsp','http', 'https', 'ftp', 'ftps', 'rtspu', 'rtsps'])]
    
    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': LocalURLFormField,
            **kwargs,
        })

class Domain(models.Model):
    domain = models.CharField(max_length=15, validators=[domain_validator], unique=True)
    description = models.CharField(max_length=100, validators=[alphanumeric_upper_space])
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain

class User(AbstractUser):
    email = models.EmailField()

class Agent(models.Model):
    name = models.CharField(max_length=50, validators=[alphanumeric_upper_space])
    uid = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, validators=[alphanumeric_upper_space])
    linked_email_account = models.EmailField()
    address = map_fields.AddressField(max_length=200, null=True)
    geolocation = map_fields.GeoLocationField(max_length=100, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    ssh_reverse_ip = models.GenericIPAddressField(blank=True, null=True)
    ssh_reverse_port = models.PositiveSmallIntegerField(blank=True, null=True)
    ssh_key_file_name = models.CharField(max_length=50, validators=[file_name_validator], blank=True, null=True)
    config_added_info = models.JSONField(blank=True, null=True)
    config_ui = models.JSONField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Camera(models.Model):
    name = models.CharField(max_length=50, validators=[alphanumeric_upper_space])
    camera_id = models.PositiveIntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    local_link = LocalURLField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
