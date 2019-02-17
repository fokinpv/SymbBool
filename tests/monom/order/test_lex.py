# pylint: disable=invalid-name
import unittest

from symbbool.monom.base import Monom
from symbbool.monom.order import Order, Lex, DegLex
from symbbool.monom import make_monom_cls, MonomBits


class TestCasesMonomLexOrder(unittest.TestCase):
    def setUp(self):
        self.monom_cls = make_monom_cls(Monom, Order, size=4)

    def test_lex(self):

        a = self.monom_cls(variables=[0])
        b = self.monom_cls(variables=[1])
        c = self.monom_cls(variables=[2])
        d = self.monom_cls(variables=[3])
        _0 = self.monom_cls.zero()
        _1 = self.monom_cls.one()

        # a > b > c > d
        self.assertFalse(Lex.lt(a, b))  # a > b
        self.assertFalse(Lex.lt(b, b))  # b > b
        self.assertTrue(Lex.lt(b, a))   # b < a
        self.assertTrue(Lex.lt(d, c))   # c < d

        self.assertFalse(Lex.lt(a, _1))  # a > 1
        self.assertTrue(Lex.lt(_1, a))  # 1 < a

        self.assertTrue(Lex.lt(_0, a))  # 0 < a
        self.assertTrue(Lex.lt(_0, _1))  # 0 < 1

        self.assertFalse(Lex.lt(a, _0))  # a > 0
        self.assertFalse(Lex.lt(_1, _0))  # 1 > 0

        ab = self.monom_cls(variables=[0, 1])
        bc = self.monom_cls(variables=[1, 2])

        # bc < a < ab
        self.assertTrue(Lex.lt(a, ab))  # a < ab
        self.assertTrue(Lex.lt(bc, a))  # bc < a
        self.assertTrue(Lex.lt(bc, ab))  # bc < ab

        abc = self.monom_cls(variables=[0, 1, 2])
        bcd = self.monom_cls(variables=[1, 2, 3])

        # bcd < abc
        self.assertTrue(Lex.lt(bcd, abc))  # bcd < abc
        self.assertFalse(Lex.lt(abc, bcd))  # abc > bcd

class TestMonomBitsLexOrder(TestCasesMonomLexOrder):
    def setUp(self):
        self.monom_cls = make_monom_cls(MonomBits, Lex, size=4)
