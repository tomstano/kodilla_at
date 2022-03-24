"""Module 1.3 - Zadanie: faktoryzacja"""

from typing import Union


def prime_factors(number: int) -> Union[list, list[int]]:
    """
    Return prime factor list for a given number.
    Assume that `number` is int.
    Raise ValueError `number` is not int.
    If number equal 1 return empty list.
    """

    if not isinstance(number, int):
        raise ValueError("number must be int!")

    pass


if __name__ == "__main__":
    print(prime_factors(number=3958159172))
