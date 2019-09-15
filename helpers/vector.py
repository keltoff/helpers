import math
from angles import AngleBase, AngleDiff


class Vector(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(Vector, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self + other.__neg__()

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __neg__(self):
        return self * (-1)

    @classmethod
    def cis(cls, angle, length=1.0):
        if isinstance(angle, AngleBase):
            angle = angle.rad

        return cls(math.cos(angle) * length, math.sin(angle) * length)

    @property
    def angle(self):
        return AngleDiff(math.atan2(self.y, self.x))

    @property
    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
