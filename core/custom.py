from django.core.validators import RegexValidator


domain_validator = RegexValidator (r'^[a-z]*$', 'Only lowercase letters are allowed')

alphanumeric_upper_space = RegexValidator(r'^[0-9A-Z\s-]*$', 'Only uppercase letters, numbers and spaces allowed')

file_name_validator = RegexValidator(r'^[\w\-. ]+$', 'Invalid file name')

alphanumeric_upper = RegexValidator(r'^[0-9A-Z]*$', 'Only uppercase letters and numbers are allowed, no spaces or special characters.')