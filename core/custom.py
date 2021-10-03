from django.core.validators import RegexValidator



domain_validator = RegexValidator (r'^[a-z]*$', 'Only lowercase letters are allowed')