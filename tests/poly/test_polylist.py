from symbbool.monom import MonomBits, make_monom_cls
from symbbool.monom.order import Order
from symbbool.poly import PolyList, make_poly_cls

from .base_cases import BasicTestCases


class TestPolyList(BasicTestCases):
    def setUp(self):
        monom_cls = make_monom_cls(MonomBits, 8, Order)
        self.poly_cls = make_poly_cls(PolyList, monom_cls)
