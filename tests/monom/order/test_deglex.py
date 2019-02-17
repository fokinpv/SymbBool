# pylint: disable=invalid-name
import unittest

from symbbool.monom.base import Monom
from symbbool.monom.order import Order, DegLex
from symbbool.monom import make_monom_cls, MonomBits


class TestCasesMonomDegLexOrder(unittest.TestCase):
    def setUp(self):
        self.monom_cls = make_monom_cls(Monom, Order, size=4)

    def test_deglex(self):
        a = self.monom_cls(variables=[0])
        b = self.monom_cls(variables=[1])
        c = self.monom_cls(variables=[2])
        d = self.monom_cls(variables=[3])
        _0 = self.monom_cls.zero()
        _1 = self.monom_cls.one()

        self.assertFalse(DegLex.lt(a, b))
        self.assertFalse(DegLex.lt(b, c))
        self.assertFalse(DegLex.lt(c, d))
        self.assertFalse(DegLex.lt(a, d))

        self.assertFalse(DegLex.lt(a, _1))  # a > 1
        self.assertTrue(DegLex.lt(_1, a))  # 1 < a

        self.assertTrue(DegLex.lt(_0, a))  # 0 < a
        self.assertTrue(DegLex.lt(_0, _1))  # 0 < 1

        self.assertFalse(DegLex.lt(a, _0))  # a > 0
        self.assertFalse(DegLex.lt(_1, _0))  # 1 > 0

        ab = self.monom_cls(variables=[0, 1])
        bc = self.monom_cls(variables=[1, 2])

        # a < bc < ab
        self.assertTrue(DegLex.lt(a, ab))
        self.assertFalse(DegLex.lt(ab, a))

        self.assertTrue(DegLex.lt(a, bc))
        self.assertFalse(DegLex.lt(bc, a))

        self.assertTrue(DegLex.lt(bc, ab))
        self.assertFalse(DegLex.lt(ab, bc))

        abc = self.monom_cls(variables=[0, 1, 2])
        bcd = self.monom_cls(variables=[1, 2, 3])

        # bcd < abc
        self.assertTrue(DegLex.lt(bcd, abc))
        self.assertFalse(DegLex.lt(abc, bcd))


class TestMonomBitsDegLexOrder(TestCasesMonomDegLexOrder):
    def setUp(self):
        self.monom_cls = make_monom_cls(MonomBits, DegLex, size=4)

