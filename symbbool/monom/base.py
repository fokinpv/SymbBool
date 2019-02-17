from functools import partialmethod


def make_monom_cls(monom_cls, order_cls, size):

    class _monom(monom_cls):
        __init__ = partialmethod(monom_cls.__init__, order_cls, size)
    return _monom


class Monom:
    def __init__(self, order_cls, size, variables=None):
        self.order = order_cls
        self.size = size

        self._init_vars(variables)

    def _init_vars(self, variables):
        raise NotImplementedError

    def __eq__(self, other):
        return NotImplemented

    def __lt__(self, other):
        return self.order.lt(self, other)

    def __le__(self, other):
        return NotImplemented

    def __gt__(self, other):
        return not self.order.lt(self, other)

    def __ge__(self, other):
        return NotImplemented

    def is_zero(self):
        raise NotImplementedError

    def is_one(self):
        raise NotImplementedError

    @classmethod
    def zero(cls):
        raise NotImplementedError

    @classmethod
    def one(cls):
        raise NotImplementedError

    @property
    def degree(self):
        raise NotImplementedError

    @property
    def vector(self):
        raise NotImplementedError
