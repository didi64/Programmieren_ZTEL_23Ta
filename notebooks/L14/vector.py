import math


class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vec2d(-self.x, -self.y)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if isinstance(other, Vec2d):
            return self.x * other.x + self.y * other.y
        else:
            return Vec2d(other*self.x, other*self.y)

    def norm(self):
        return (self*self) ** 0.5

    def unit(self, err=1E-10):
        if self.norm() < err:
            return Vec2d(1, 0)
        return self * (1/self.norm())

    def closest(self, vecs):
        return min(vecs, key=lambda v: (v-self).norm())

    def perp(self):
        return Vec2d(-self.y, self.x)

    def angle(self, other, signed=True, degree=False):
        deg = 180 / math.pi if degree else 1
        alpha = deg * math.acos(self.unit() * other.unit())
        if signed:
            sign = -1 if self.area(other, signed=True) < 0 else 1
        return sign * alpha

    def area(self, other, signed=True):
        a = self.perp() * other
        return a if signed else abs(a)

    def as_tuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return 'Vec({}, {})'.format(self.x, self.y)
