import unittest

from .test_polylist import TestPolyList
from .test_polyzdd import TestPolyZDD


def load_tests(loader, tests, pattern):
    test_cases = (TestPolyList, TestPolyZDD,)

    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = loader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)

    return suite
