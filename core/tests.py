from .custom import alphanumeric_upper_space, domain_validator, file_name_validator, alphanumeric_upper
from .models import Agent, Domain, MetaData
import pytest
from django.core.exceptions import ValidationError

# custom file

@pytest.mark.parametrize('correct_value, incorrect_value', 
                        [('okokok', '1okook'),
                        ('subdomain','SUBDOMAIN')
                        ])
def test_domain_validator(correct_value, incorrect_value):
    val = domain_validator(value=correct_value)
    with pytest.raises(ValidationError) as e_info:
        val2 = domain_validator(value=incorrect_value)

@pytest.mark.parametrize(['correct_value', 'incorrect_value'], 
                        [('OKOKOK OKOK', '1okook'),
                         ('HOLA','Hola')
                        ])
def test_alphanumeric_upper_space(correct_value, incorrect_value):
    val = alphanumeric_upper_space(value=correct_value)
    with pytest.raises(ValidationError) as e_info:
        val = alphanumeric_upper_space(value=incorrect_value)


@pytest.mark.parametrize(['correct_value', 'incorrect_value'], 
                        [('OKOKOKOK11OK', '1okook'),
                         ('AABB23','HOLA HOLA')
                        ])
def test_alphanumeric_upper(correct_value, incorrect_value):
    val = alphanumeric_upper(value=correct_value)
    with pytest.raises(ValidationError) as e_info:
        val = alphanumeric_upper(value=incorrect_value)

@pytest.mark.parametrize(['correct_value', 'incorrect_value'], 
                        [('file.txt', '*.123*'),
                         ('file','$$file.txt')
                        ])
def test_file_name_validator(correct_value, incorrect_value):
    val = file_name_validator(value=correct_value)
    with pytest.raises(ValidationError) as e_info:
        val = file_name_validator(value=incorrect_value)


