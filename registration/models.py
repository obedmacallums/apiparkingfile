from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from core.models import Domain
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=True, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True)
    telegram_id = models.BigIntegerField(blank=True, null=True)
    email_notify = models.BooleanField(default = True)
    sms_notify = models.BooleanField(default = False)
    telegram_notify = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return  self.user.username + "_profile"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def ensure_profile_exists(sender, instance, **kwargs):
    
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)