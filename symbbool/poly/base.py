"""Implements an interface for a polynomial class."""
from functools import partialmethod


def make_poly_cls(poly_cls, monom_cls):
    """Construct new polynomial class with a given Monom class."""
    class _poly(poly_cls):
        __init__ = partialmethod(poly_cls.__init__, monom_cls)
    return _poly


class Poly:
    def __init__(self, monom_cls, var=None, monom=None, monoms=None):
        self.monom_cls = monom_cls

        is_monoms = monoms is not None
        is_var = var is not None
        is_monom = monom is not None

        # We want zero or one parameter
        if [is_monoms, is_var, is_monom].count(True) > 1:
            raise RuntimeError("Only one initialization parameter is allowed")

        if is_monoms:
            self._init_monoms(monoms)
        elif is_var:
            self._init_var(var)
        elif is_monom:
            self._init_monom(monom)
        else:
            raise NotImplementedError

    def _init_monoms(self, monoms):
        raise NotImplementedError

    def _init_var(self, var):
        raise NotImplementedError

    def _init_monom(self, monom):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    @classmethod
    def make_zero(cls):
        raise NotImplementedError

    @classmethod
    def make_one(cls):
        raise NotImplementedError

    def is_one(self):
        raise NotImplementedError

    def is_zero(self):
        raise NotImplementedError

    def lm(self):  # pylint: disable=invalid-name
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError
