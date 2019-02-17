# pylint: disable=invalid-name
import unittest

from symbbool.monom.base import Monom
from symbbool.monom.order import Order, DegRevLex
from symbbool.monom import make_monom_cls, MonomBits


class TestCasesMonomDegRevLexOrder(unittest.TestCase):
    def setUp(self):
        self.monom_cls = make_monom_cls(Monom, Order, size=4)

    def test_degrevlex(self):
        a = self.monom_cls(variables=[0])
        b = self.monom_cls(variables=[1])
        c = self.monom_cls(variables=[2])
        d = self.monom_cls(variables=[3])
        _0 = self.monom_cls.zero()
        _1 = self.monom_cls.one()

        # a < b < c < d
        self.assertTrue(DegRevLex.lt(a, b))
        self.assertFalse(DegRevLex.lt(b, a))

        self.assertFalse(DegRevLex.lt(c, b))
        self.assertFalse(DegRevLex.lt(d, c))
        self.assertFalse(DegRevLex.lt(d, a))

        self.assertFalse(DegRevLex.lt(a, _1))  # a > 1
        self.assertTrue(DegRevLex.lt(_1, a))  # 1 < a

        self.assertFalse(DegRevLex.lt(a, _0))  # a > 0
        self.assertFalse(DegRevLex.lt(_1, _0))  # 1 > 0

        self.assertTrue(DegRevLex.lt(_0, a))  # 0 < a
        self.assertTrue(DegRevLex.lt(_0, _1))  # 0 < 1

        ab = self.monom_cls(variables=[0, 1])
        bc = self.monom_cls(variables=[1, 2])

        # a < ab < bc
        self.assertFalse(DegRevLex.lt(ab, a))
        self.assertFalse(DegRevLex.lt(bc, a))
        self.assertFalse(DegRevLex.lt(bc, ab))

        abc = self.monom_cls(variables=[0, 1, 2])
        bcd = self.monom_cls(variables=[1, 2, 3])

        # abc < bcd
        self.assertFalse(DegRevLex.lt(bcd, abc))
        self.assertTrue(DegRevLex.lt(abc, bcd))


class TestMonomBitsDegRevLexOrder(TestCasesMonomDegRevLexOrder):
    def setUp(self):
        self.monom_cls = make_monom_cls(MonomBits, DegRevLex, size=4)
