"""Module 1.1 - Zadanie: palindromy"""

from typing import Union


def is_palindrome(data: Union[str, int, list, None]) -> Union[bool, str]:
    """
    Return True if `data` is palindrome, False otherwise.
    Assume that `data` is lowercase letters.
    """

    if not data:
        raise ValueError("No given data!")

    if isinstance(data, (str, int)):
        data = str(data).lower()
        if data == data[::-1]:
            return True
        else:
            return False

    elif isinstance(data, list):
        my_list = ' '.join([str(elem) for elem in data]).lower()
        return is_palindrome(my_list)

    else:
        return "Incompatible data type!"


if __name__ == "__main__":
    try:
        is_palindrome(data=None)
    except ValueError:
        print("Correct -> given data is None")

    assert is_palindrome(data="malayalam") is True
    assert is_palindrome(data="Malayalam") is True
    assert is_palindrome(data="MalAYAlaM") is True
    assert is_palindrome(data="tomek") is False

    assert is_palindrome(data=12321) is True
    assert is_palindrome(data=1232144) is False
    assert is_palindrome(data=[1, 2, 3, 2, 1]) is True
    assert is_palindrome(data=[1, 2, 3, 2, 1, 3, 5, None]) is False

    assert is_palindrome(data={1, 2, 3, 2, 1}) == "Incompatible data type!"
    assert is_palindrome(data=(1, 2, 3, 2, 1)) == "Incompatible data type!"





