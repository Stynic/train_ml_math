class Fraction:
    def __init__(self, num: int or str, dem: int or str = 0):
        self.fraction = num + dem / 10 if num > 0 else num - dem / 10

    def __str__(self):
        return str(self.fraction)

    def __int__(self):
        return int(self.fraction)

    def __float__(self):
        return self.fraction

    def __repr__(self):
        return str(self.fraction)

    def __add__(self, other):
        _num, _dem = str(round(self.fraction + other.fraction, 1)).split('.')
        return Fraction(int(_num), int(_dem))

    def __sub__(self, other):
        _num, _dem = str(round(self.fraction - other.fraction, 1)).split('.')
        return Fraction(int(_num), int(_dem))

    def __mul__(self, other):
        _num, _dem = str(round(self.fraction * other.fraction, 1)).split('.')
        return Fraction(int(_num), int(_dem))

    def __truediv__(self, other):
        _num, _dem = str(round(self.fraction / other.fraction, 1)).split('.')
        return Fraction(int(_num), int(_dem))


class OperationsOnFraction(Fraction):
    def getint(self):
        return int(self)

    def getfloat(self):
        return float(self)


if __name__ == '__main__':
    print(Fraction(3, 1) + Fraction(2, 8))
    print(Fraction(4, 7) + Fraction(3, 1))

