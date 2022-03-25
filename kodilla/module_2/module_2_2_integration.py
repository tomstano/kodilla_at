"""Module 2.2 - Zadanie: systemy liczbowe

UT added in ./tests/test_module_2_2_integration.py
"""

import re
from typing import ClassVar


class RomanNumericConverter:
    ROMAN_PAIRS: ClassVar[list[set]] = [('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10), ('XL', 40), ('L', 50),
                                        ('XC', 90), ('C', 100), ('CD', 400), ('D', 500), ('CM', 900), ('M', 1000)]
    REVERSED_PAIRS: ClassVar[list[set]] = ROMAN_PAIRS[::-1]

    @classmethod
    def _to_number(cls, rom: str, num: int = 0) -> int:
        """Convert to 'int' from roman number."""

        for val in cls.REVERSED_PAIRS:
            if rom.startswith(val[0]):
                num += val[1]
                rom = rom[len(val[0]):]
                return cls._to_number(rom, num)
        return num

    @classmethod
    def _to_roman(cls, num: int, rom: str = "") -> str:
        """Convert to roman number from 'int'."""

        for val in cls.REVERSED_PAIRS:
            if num >= val[1]:
                return cls._to_roman(num - val[1], rom + val[0])
        return rom

    def converter(self, val: str | int) -> str | int:
        """
        A base function that accumulates value conversions for:
        - from 'roman' to 'number'
        - from 'number' to 'roman'
        """
        result: str | int

        if isinstance(val, int):
            if not 0 < val < 4000:
                raise ValueError("Max or min number exceeded!")
            else:
                result = self._to_roman(val)
        elif isinstance(val, str):
            _match_regex = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
            if _match_regex.match(val):
                result = self._to_number(val)
            else:
                raise ValueError('invalid input from str type value!')
        else:
            raise ValueError("invalid value -> expected type: str, int!")

        return result


if __name__ == "__main__":
    # class instance:
    conv = RomanNumericConverter()

    # correct tests:
    print(conv.converter(val=50))
    print(conv.converter(val='L'))
    print(conv.converter(val=1986))
    print(conv.converter(val='CMXC'))

    # raise ValueError with msg:
    print(conv.converter(val=19323243243242342386))
    print(conv.converter(val='NotCorrectString'))
    print(conv.converter(val=None))  # noqa
    print(conv.converter(val=0.1))  # noqa
