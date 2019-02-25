from .base import Monom


class MonomBits(Monom):
    def _init_vars(self, variables):
        if variables is None:
            self._bits = tuple()
        else:
            bits = [0] * self.size
            for var in variables:
                bits[var] = 1
            self._bits = tuple(bits)

    def __eq__(self, other):
        return self._bits == other._bits

    def is_zero(self):
        return self._bits == ()

    def is_one(self):
        return self._bits == (0,)

    @classmethod
    def zero(cls):
        zero = cls()
        zero._bits = tuple()
        return zero

    @classmethod
    def one(cls):
        one = cls()
        one._bits = (0,)
        return one

    @property
    def degree(self):
        return sum(self._bits)

    @property
    def vector(self):
        return self._bits
