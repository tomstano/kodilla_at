"""Module 1.3 - Zadanie: faktoryzacja / UT"""

import unittest
from module_1_3_TDD_prime_factors import prime_factors


class TestPrimeFactor(unittest.TestCase):
    """Class for test prime_factor function."""

    def test_import_prime_factors(self):
        try:
            from module_1_3_TDD_prime_factors import prime_factors
            assert callable(prime_factors), "prime_factors not callable"
        except ImportError as err:
            assert False, err

    def test_prime_factor_number_is_int(self):
        with self.assertRaises(ValueError) as exc:
            prime_factors(number='test')

        with self.assertRaises(ValueError):
            prime_factors(number=0.1)

    def test_prime_factor_value_err_msg(self):
        try:
            prime_factors(number='test')
        except Exception as exc:
            self.assertEqual(str(exc), "number must be int!")

    def test_prime_factor_number_set_as_1_return_empty_list(self):
        self.assertEqual(prime_factors(1), [])

    def test_prime_factor_kodilla_case(self):
        self.assertEqual(prime_factors(number=3958159172), [2, 2, 11, 2347, 38329])

    def test_get_multiple_call_prime_factor_with_different_numbers(self):
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(6), [2, 3])
        self.assertEqual(prime_factors(7), [7])
        self.assertEqual(prime_factors(8), [2, 2, 2])
        self.assertEqual(prime_factors(9), [3, 3])
        self.assertEqual(prime_factors(17), [17])


if __name__ == '__main__':
    unittest.main()
