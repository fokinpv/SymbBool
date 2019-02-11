import unittest

from symbbool.monom.base import Monom
from symbbool.monom.order import Order
from symbbool.monom import make_monom_cls


class BasicTestCases(unittest.TestCase):
    def setUp(self):
        self.monom_cls = make_monom_cls(Monom, Order, size=4)

    def test_init_empty(self):
        monom = self.monom_cls()
        self.assertTrue(monom.is_zero())
