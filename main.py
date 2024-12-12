import math


class Complex:
    def __init__(self, real=1.0, imag=0.0):
        self.real = real
        self.imag = imag

    def Re(self):
        return self.real

    def Im(self):
        return self.imag

    def Abs(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def Arg(self):
        return math.atan2(self.imag, self.real)

    def __invert__(self):
        return Complex(self.real, -self.imag)

    def Pow(self, deg):
        if deg == 0:
            return Complex(1, 0)

        n = abs(deg)
        result = Complex(1, 0)
        base = self

        while n > 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2

        return result if deg > 0 else Complex(1, 0) / result

    def Rt(self, n):
        roots = []
        r = self.Abs() ** (1 / n)
        angle = self.Arg()
        for k in range(n):
            theta = (angle + 2 * math.pi * k) / n
            roots.append(Complex(r * math.cos(theta), r * math.sin(theta)))
        return roots

    def Rt_one(self, n, k):
        r = self.Abs() ** (1 / n)
        theta = (self.Arg() + 2 * math.pi * k) / n
        return Complex(r * math.cos(theta), r * math.sin(theta))

    def __eq__(self, other):
        return math.isclose(self.real, other.real) and math.isclose(self.imag, other.imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / denominator,
                       (self.imag * other.real - self.real * other.imag) / denominator)

    def __iadd__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self

    def __isub__(self, other):
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __imul__(self, other):
        result = self * other
        self.real, self.imag = result.real, result.imag
        return self

    def __itruediv__(self, other):
        result = self / other
        self.real, self.imag = result.real, result.imag
        return self

    def __str__(self):
        if self.real != 0 and self.imag != 0:
            return f"{self.real} {'+' if self.imag > 0 else '-'} {abs(self.imag)}i"
        elif self.real == 0 and self.imag != 0:
            return f"{self.imag}i"
        elif self.imag == 0:
            return f"{self.real}"
        else:
            return "0"

    def __repr__(self):
        return self.__str__()
