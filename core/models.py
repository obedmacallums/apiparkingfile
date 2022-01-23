from django.db import models
from .custom import domain_validator, alphanumeric_upper_space, file_name_validator, alphanumeric_upper, JSONSchemaValidator
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

class MetaData(models.Model):
    MY_JSON_FIELD_SCHEMA = {    
    'type': 'object'
    }

    meta_data = models.JSONField(validators=[JSONSchemaValidator(limit_value=MY_JSON_FIELD_SCHEMA)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "meta data"



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

class Category(models.Model):
    name =  models.CharField(max_length=50, validators=[alphanumeric_upper_space])
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"        
        constraints = [
        models.UniqueConstraint(fields= ['name','agent'], name='unique_name_agent'),
        ]

class AddedInfo(models.Model):
    plate = models.CharField(max_length=8, validators=[alphanumeric_upper])
    driver_name = models.CharField(max_length=100, validators=[alphanumeric_upper_space], blank=True, null=True)
    driver_id = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    custom_fields = models.JSONField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "added info"

    def __str__(self):
        return self.plate



class Entry(models.Model):
    plate = models.CharField(max_length=8, validators=[alphanumeric_upper])

    camara = models.ForeignKey(Camera, null=True, on_delete=models.SET_NULL)
    agent = models.ForeignKey(Agent, null=True, on_delete=models.SET_NULL)
    
    confidence = models.FloatField(blank=True, null=True)
    travel_direction = models.FloatField(blank=True, null=True)

    vehicle = models.JSONField(blank=True, null=True)
    
    is_parked = models.BooleanField(default=False)
    is_preview = models.BooleanField(default=False)
    vehicle_detected = models.BooleanField(default=False)
    
    best_uuid = models.CharField(max_length=100, blank=True, null=True)
    link_image = models.URLField (blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    crop_image = models.TextField(blank=True, null=True)

    driver_name = models.CharField(max_length=100, validators=[alphanumeric_upper_space], blank=True, null=True)
    driver_id = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, default=None)
    custom_fields = models.JSONField(blank=True, null=True)

    meta_data = models.OneToOneField(MetaData, null=True, on_delete=models.SET_NULL)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate



