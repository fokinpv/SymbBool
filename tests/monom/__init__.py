import unittest

from .test_monom_bits import TestMonomBits


def load_tests(loader, tests, pattern):
    test_cases = (TestMonomBits,)

    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)

    return suite
