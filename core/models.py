from django.db import models
from .custom import domain_validator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()


class Domain(models.Model):
    domain = models.CharField(max_length=15, validators=[domain_validator], unique=True)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain

