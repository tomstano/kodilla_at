"""Module 2.2 - Zadanie: systemy liczbowe / UT - pytest

Run tests from ./kodilla_at directory:
    cmd: pytest -vvv

Requirements:
    pytest -> pip install -r /path/to/requirements.txt
"""

import pytest
from kodilla.module_2.module_2_2_integration import RomanNumericConverter


def test_import_rom_num_converter():
    try:
        assert callable(RomanNumericConverter), "RomanNumericConverter not callable"
    except ImportError as err:
        assert False, err


@pytest.fixture(name="roman_num_instance")
def roman_numeric_converter_init():
    class_instance = RomanNumericConverter()
    return class_instance


@pytest.mark.parametrize(
    ('number', 'expected'),
    [
        (1, 'I'),
        (2, 'II'),
        (4, 'IV'),
        (5, 'V'),
        (9, 'IX'),
        (990, 'CMXC'),
        (1986, 'MCMLXXXVI'),
    ]
)
def test_to_roman_returns_correct_result(roman_num_instance, number, expected):
    assert roman_num_instance.converter(number) == expected


@pytest.mark.parametrize(
    ('number', 'expected'),
    [
        ('I', 1),
        ('II', 2),
        ('IV', 4),
        ('V', 5),
        ('IX', 9),
        ('CMXC', 990),
        ('MCMLXXXVI', 1986),
    ]
)
def test_from_roman_returns_correct_result(roman_num_instance, number, expected):
    assert roman_num_instance.converter(number) == expected


def test_converter_raise_value_error_when_value_exceed_min_or_max(roman_num_instance):
    with pytest.raises(ValueError) as error:
        roman_num_instance.converter(val=32432432432421341)
    assert str(error.value) == "Max or min number exceeded!"


def test_converter_raise_value_error_when_str_value_is_not_correct(roman_num_instance):
    with pytest.raises(ValueError) as error:
        roman_num_instance.converter(val="NotCorrectString")
    assert str(error.value) == 'invalid input from str type value!'


@pytest.mark.parametrize('not_supported_types', [None, 0.1])
def test_converter_raise_value_error_when_str_value_is_none(roman_num_instance, not_supported_types):
    with pytest.raises(ValueError) as error:
        roman_num_instance.converter(val=not_supported_types)  # noqa
    assert str(error.value) == 'invalid value -> expected type: str, int!'

