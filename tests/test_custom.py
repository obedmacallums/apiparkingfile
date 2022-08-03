import pytest

from core.custom import validate_rut_module_11, compare_equal_strings

def test_rut():
    assert validate_rut_module_11("25907391-k") == True
    assert validate_rut_module_11("25907391-8") == False
    assert validate_rut_module_11("25907391") == False

def test_compare_string():
    assert compare_equal_strings("123456", "123456", 0) == True
    assert compare_equal_strings("123456", "123458", 1) == True
    assert compare_equal_strings("123456", "12348", 2) == True
    assert compare_equal_strings("123456", "123456", 1) == True
    assert compare_equal_strings("123456", "12348", 1) == False


