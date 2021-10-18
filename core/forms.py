from django.core import validators
from django.forms.fields import URLField as FormURLField

class LocalURLFormField(FormURLField):
    default_validators = [validators.URLValidator(schemes=['rtsp','http', 'https', 'ftp', 'ftps', 'rtspu', 'rtsps'])]