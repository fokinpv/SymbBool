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

    def test_zero(self):
        monom = self.monom_cls.zero()
        self.assertTrue(monom.is_zero())

    def test_one(self):
        monom = self.monom_cls.one()
        self.assertTrue(monom.is_one())

    def test_degree(self):
        monom = self.monom_cls.zero()
        self.assertTrue(monom.degree == 0)

        monom = self.monom_cls.one()
        self.assertTrue(monom.degree == 0)

        monom = self.monom_cls(variables=[0])
        self.assertTrue(monom.degree == 1)

        monom = self.monom_cls(variables=[0, 1, 2])
        self.assertTrue(monom.degree == 3)

    def test_equal(self):
        monom1 = self.monom_cls(variables=[0])
        monom2 = self.monom_cls(variables=[0])
        zero1 = self.monom_cls.zero()
        zero2 = self.monom_cls.zero()

        one1 = self.monom_cls.zero()
        one2 = self.monom_cls.zero()

        self.assertTrue(monom1 == monom2)
        self.assertTrue(zero1 == zero2)
        self.assertTrue(one1 == one2)

    def test_not_equal(self):
        monom1 = self.monom_cls(variables=[0])
        monom2 = self.monom_cls(variables=[1])
        zero = self.monom_cls.zero()
        one = self.monom_cls.one()

        self.assertTrue(monom1 != monom2)
        self.assertTrue(zero != one)
