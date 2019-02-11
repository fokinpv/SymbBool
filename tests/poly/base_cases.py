import unittest

from symbbool.poly import make_poly_cls
from symbbool.poly.base import Poly
from symbbool.monom import MonomBits, make_monom_cls
from symbbool.monom.order import Order


class BasicTestCases(unittest.TestCase):
    def setUp(self):
        self.monom_cls = make_monom_cls(MonomBits, Order, 8)
        self.poly_cls = make_poly_cls(Poly, self.monom_cls)

    #  @unittest.skip('Not implemented')
    def test_init_empty(self):
        with self.assertRaises(NotImplementedError):
            self.poly_cls()

    #  @unittest.skip('Not implemented')
    def test_init_var(self):
        self.poly_cls(var=0)

    #  @unittest.skip('Not implemented')
    def test_init_monom(self):
        self.poly_cls(monom=0)

    #  @unittest.skip('Not implemented')
    def test_init_monoms(self):
        self.poly_cls(monoms=0)
