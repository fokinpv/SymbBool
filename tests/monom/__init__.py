import unittest

from .test_monom_bits import TestMonomBits
from .order.test_lex import TestMonomBitsLexOrder
from .order.test_deglex import TestMonomBitsDegLexOrder
from .order.test_degrevlex import TestMonomBitsDegRevLexOrder


def load_tests(loader, tests, pattern):
    test_cases = (
        TestMonomBits,
        TestMonomBitsLexOrder,
        TestMonomBitsDegLexOrder,
        TestMonomBitsDegRevLexOrder,
    )

    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)

    return suite
