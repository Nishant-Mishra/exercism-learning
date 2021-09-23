"""
    A complex number is a number in the form a + b * i where a and b are real and i satisfies i^2 = -1.

    `a` is called the real part and `b` is called the imaginary part of `z`.
    The conjugate of the number `a + b * i` is the number `a - b * i`.
    The absolute value of a complex number `z = a + b * i` is a real number `|z| = sqrt(a^2 + b^2)`.
    The square of the absolute value `|z|^2` is the result of multiplication of `z` by its complex conjugate.

    The sum/difference of two complex numbers involves adding/subtracting their real and imaginary parts separately:
        `(a + i * b) + (c + i * d) = (a + c) + (b + d) * i`,
        `(a + i * b) - (c + i * d) = (a - c) + (b - d) * i.`

    Multiplication result is by definition `(a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i`.

    The reciprocal of a non-zero complex number is `1 / (a + i * b) = a/(a^2 + b^2) - b/(a^2 + b^2) * i`.

    Dividing a complex number a + i * b by another c + i * d gives:
        `(a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i`.

    Raising `e` to a complex exponent can be expressed as:
        `e^(a + i * b) = e^a * e^(i * b)`,
        the last term of which is given by Euler's formula `e^(i * b) = cos(b) + i * sin(b)`.

    Task:
        Implement the following operations:

        - addition, subtraction, multiplication and division of two complex numbers,
        - conjugate, absolute value, exponent of a given complex number.

    Assume the programming language you are using does not have an implementation of complex numbers.
"""
from math import sqrt, cos, sin, exp
from typing import Union


class ComplexNumber:
    """
        A Class to emulate Complex Numbers
    """
    REAL_SET = {int, float}

    def __init__(self, real: Union[int, float], imaginary: Union[int, float] = 0):
        self._real = real
        self._imag = imaginary
        self._validate()

    def _validate(self):
        if (type(self.real) not in self.REAL_SET or
           type(self.imaginary) not in self.REAL_SET):
            raise ValueError("Both the real and imaginary parts of the complex number must be real!!")

    @property
    def real(self):
        """

        :return: Real part of the Complex Number
        """
        return self._real

    @property
    def imaginary(self):
        """

        :return: Imaginary part of the Complex Number
        """
        return self._imag

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return self.__class__(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return self.__class__(self.real * other.real - self.imaginary * other.imaginary,
                              self.real * other.imaginary + self.imaginary * other.real)

    def __sub__(self, other):
        return self + self.__class__(-other.real, -other.imaginary)

    # Since the square of absolute value of a Complex Number will have `imaginary == 0`
    def _abs_square(self):
        return (self * self.conjugate()).real

    def _reciprocal(self):
        return self.__class__(self.real / self._abs_square(),
                              -self.imaginary / self._abs_square())

    def __truediv__(self, other):
        return self * other._reciprocal()

    def __abs__(self):
        return sqrt(self._abs_square())

    def conjugate(self):
        """

        :return: The Complex Conjugate of the Complex Number
        """
        return self.__class__(self.real, -self.imaginary)

    # Calculate value of e^ib as per Euler's Formula
    def _exp_imag_only(self):
        return self.__class__(cos(self.imaginary), sin(self.imaginary))

    def exp(self):
        """

        :return: The value of `e` raised to the power of the Complex Number
        """
        return self.__class__(exp(self.real)) * self._exp_imag_only()
