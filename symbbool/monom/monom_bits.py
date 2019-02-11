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

    def is_zero(self):
        return self._bits == ()

    def is_one(self):
        return self._bits == (0,)

    @classmethod
    def zero(cls):
        return cls(bits=tuple())

    @classmethod
    def one(cls):
        return cls(bits=(0,))

    @property
    def degree(self):
        return sum(self._bits)
