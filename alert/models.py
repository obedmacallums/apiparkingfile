from django.db import models
from django.conf import settings
from django.db.models.enums import Choices
from core.custom import alphanumeric_upper
from core.models import Camera, Category

# Create your models here.

class ConfigAlert(models.Model):
    class Precision(models.IntegerChoices):
        EQUAL = 0
        OVER_80 = 1
        OVER_60 = 2
    
    plate_pattern = models.CharField(max_length=8, validators=[alphanumeric_upper])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    camera = models.ForeignKey (Camera, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    alert_time = models.JSONField()
    precision = models.IntegerField(choices=Precision.choices)
    match_by_category = models.BooleanField(default=False)

    any_plate = models.BooleanField(default=False)


    category = models.ManyToManyField(Category, default=None, blank=True)

  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.plate_pattern
