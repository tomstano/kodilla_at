"""Module 1.3 - Zadanie: faktoryzacja / UT"""

import unittest
from module_1_3_TDD_prime_factors import prime_factors


class TestPrimeFactor(unittest.TestCase):
    """ Class for test get prime factor """

    def test_import_prime_factors(self):
        try:
            from module_1_3_TDD_prime_factors import prime_factors
            assert callable(prime_factors), "prime_factors not callable"
        except ImportError as err:
            assert False, err

    def test_pf_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            prime_factors(number=1)


if __name__ == '__main__':
    unittest.main()
