from symbbool.monom import make_monom_cls, MonomBits
from symbbool.monom.order import Order, Lex

from .base_cases import BasicTestCases


class TestMonomBits(BasicTestCases):
    def setUp(self):
        self.monom_cls = make_monom_cls(MonomBits, Lex, size=4)

    def test_init_variables(self):
        monom = self.monom_cls(variables=[0])
        self.assertEqual(monom._bits, (1, 0, 0, 0))
