from symbbool.monom import MonomBits, make_monom_cls
from symbbool.monom.order import Order
from symbbool.poly import PolyZDD, make_poly_cls

from .base_cases import BasicTestCases


class TestPolyZDD(BasicTestCases):
    def setUp(self):
        monom_cls = make_monom_cls(MonomBits, Order, 8)
        self.poly_cls = make_poly_cls(PolyZDD, monom_cls)
