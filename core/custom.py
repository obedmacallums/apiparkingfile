from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import json
import jsonschema
from django.core.validators import BaseValidator
import difflib
import re


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
      1: almost equal. (confidence > 90%)
      2: more permissive to compare, maybe two characters can be different,
         it depends on the length of the strings to be compared.
         (90% > confidence > 70%)

    More detail https://docs.python.org/3/library/difflib.html
    '''
    valid_precision = {0, 1, 2}

    if precision not in valid_precision:
        raise ValueError("precision must between 0 and 1")
    confidence = difflib.SequenceMatcher(None, string1, string2).quick_ratio()
    print(confidence)

    if confidence == 1:
        return True

    if confidence >= 0.8 and precision >= 1:
        return True
    
    if confidence >= 0.7 and precision == 2:
        return True

    return False

def validate_rut_module_11(rut:str) -> bool :
  '''
  important:
  rut string allowed: from 6 to 10 digits + "-" character + one digit or K or k

  return True if pass module 11 validation
  return False if dont pass module 11 validation

  module 11:
  for more details view http://www.pgrocer.net/Cis51/mod11.html
  '''

  if re.search(r'^[0-9]{6,10}-[\dkK]$', rut):
    reversed_rut = rut[::-1]
    dv = reversed_rut[0]

    if dv == "k"or dv =="K":
      dv_num = 10
    elif dv == "0":
      dv_num = 11
    else:
      dv_num = int(dv)
    suma = 0
    multiplo = 1

    for x in reversed_rut[2:]:
      if multiplo < 7:
        multiplo += + 1
      else:
        multiplo = 2      
      suma += + int(x) * multiplo
    modulo11 = 11 - (suma % 11)

    if modulo11 == dv_num:
      return True
    else:
      return False
  else:
    return False