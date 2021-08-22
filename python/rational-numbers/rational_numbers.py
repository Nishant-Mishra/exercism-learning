from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        assert denom != 0, "ValueError: The denominator of the Rational Number cannot be 0"

        gcd = self._gcd(abs(numer), abs(denom))
        numer = numer // gcd
        denom = denom // gcd

        numer_sign = numer // abs(numer) if numer else 1
        denom_sign = denom // abs(denom)

        self.numer = abs(numer) if numer_sign == denom_sign else -abs(numer)
        self.denom = abs(denom)

    def _gcd(self, a, b):
        if a == 0 or a == b:
            return b
        elif b == 0:
            return a
        elif a < b:
            return self._gcd(a, b % a)
        elif a >= b:
            return self._gcd(a % b, b)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return self.__class__(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom
        )

    def __sub__(self, other):
        return self.__class__(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom
        )

    def __mul__(self, other):
        return self.__class__(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        return self.__class__(
            self.numer * other.denom,
            self.denom * other.numer
        )

    def __abs__(self):
        return self.__class__(
            abs(self.numer),
            abs(self.denom)
        )

    def __pow__(self, power):
        is_int = (power == int(power))
        sign = power // abs(power) if power else 1
        numer = pow(self.numer, power)
        denom = pow(self.denom, power)
        if is_int:
            t = (numer, denom)
            return self.__class__(*t[::sign])
        else:
            return numer / denom

    def __rpow__(self, base):
        return pow(pow(base, self.numer), 1 / self.denom)
