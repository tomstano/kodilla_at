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

    if number == 1:
        return []

    for num in range(2, number):
        a, b = divmod(number, num)
        if not b:
            ret_val = [num] + prime_factors(a)
            return ret_val

    return [number]


if __name__ == "__main__":
    print(prime_factors(1))  # empty list
    print(prime_factors(2))
    print(prime_factors(6))
    print(prime_factors(7))
    print(prime_factors(8))
    print(prime_factors(9))
    print(prime_factors(17))
    print(prime_factors(number=3958159172))  # Kodilla case
