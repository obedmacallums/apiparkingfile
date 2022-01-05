from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import json
import jsonschema
from django.core.validators import BaseValidator
import difflib


domain_validator = RegexValidator (r'^[a-z]*$', 'Only lowercase letters are allowed')

alphanumeric_upper_space = RegexValidator(r'^[0-9A-Z\s-]*$', 'Only uppercase letters, numbers and spaces allowed')

file_name_validator = RegexValidator(r'^[\w\-. ]+$', 'Invalid file name')

alphanumeric_upper = RegexValidator(r'^[0-9A-Z]*$', 'Only uppercase letters and numbers are allowed, no spaces or special characters.')




class JSONSchemaValidator(BaseValidator):
    
    def compare(self, value, schema):
        try:
            if isinstance(value, str):
                value = json.loads(value)
            jsonschema.validate(value, schema)
        except:
            raise ValidationError(f'{value} failed JSON schema check')


def compare_equal_strings(string1:str, string2:str, precision:int):
    '''
    Return True if strings are equal, False if they are different.

    Accepted precision:
      0: they are identical.
      1: almost equal. (confidence > 80%)
      2: more permissive to compare, maybe two characters can be different,
         it depends on the length of the strings to be compared.
         (80% > confidence > 60%)

    More detail https://docs.python.org/3/library/difflib.html
    '''
    valid_precision = {0,1,2}

    if precision not in valid_precision:
        raise ValueError("precision must between 0 and 2")
    confidence = difflib.SequenceMatcher(None, string1, string2).quick_ratio()

    if confidence == 1:
        return True
    elif confidence >= 0.8 and precision >= 1:
        return True
    elif 0.8 > confidence >= 0.6 and precision == 2:
        return True
    else:
        return False