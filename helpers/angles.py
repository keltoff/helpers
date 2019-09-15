import math
from numbers import Number


def limit(val):
    if val > math.pi:
        val -= 2*math.pi
    if val < -math.pi:
        val += 2*math.pi
    return val


def transform(kp, c, front):
    dx, dy = kp.pt[0] - c[0], kp.pt[1] - c[1]
    th = math.atan2(dx, dy)
    # + inverted image
    return limit(th - front)


def polar_transform(point, center, front):
    dx, dy = point.pt[0] - center[0], point.pt[1] - center[1]
    th = math.atan2(dx, dy)
    return Angle(rad=th)


class AngleBase(float):
    def __new__(cls, rad=None, deg=None):
        if rad is not None:
            if isinstance(rad, AngleBase):
                val = rad.rad
            elif isinstance(rad, Number):
                val = rad
        elif deg is not None:
            val = math.radians(deg)
        else:
            raise Exception('You actually need SOME value')

        return float.__new__(cls, cls.normalize(val))

    @property
    def deg(self):
        return math.degrees(self.rad)

    @property
    def rad(self):
        return float(self)

    @classmethod
    def normalize(cls):
        raise NotImplementedError()

    @staticmethod
    def normalize_to(value, (min, max), step):
        while value > max:
            value -= step
        while value < min:
            value += step
        return value

    @classmethod
    def from_points(cls, point, center, front):
        dx, dy = point.pt[0] - center[0], point.pt[1] - center[1]
        th = math.atan2(dx, dy)
        return cls(rad=th-front)

    def __mul__(self, other):
        return self.__class__(rad=self.rad * other)

    def __div__(self, other):
        return self.__class__(rad=self.rad / other)

    def __abs__(self):
        return self.__class__(rad=abs(self.rad))

    def __neg__(self):
        return self.__class__(rad=-1.0 * self)

    def __sub__(self, other):
        return self.__add__(-other)


class Angle(AngleBase):
    @classmethod
    def normalize(cls, val):
        return AngleBase.normalize_to(val, (0, 2 * math.pi), 2 * math.pi)

    def __add__(self, other):
        if isinstance(other, AngleDiff):
            return Angle(rad=self.rad + other.rad)
        elif isinstance(other, Angle):
            raise Warning('Should you really be summing two absolute angles?')
            return Angle(rad=self.rad + other.rad)
        elif isinstance(other, Number):
            return Angle(rad=self.rad + other)
        else:
            raise NotImplementedError()

    def __sub__(self, other):
        if other.__class__ == Angle:
            return AngleDiff(self.rad - other.rad)
        else:
            return AngleBase.__sub__(self, other)


class AngleDiff(AngleBase):
    @classmethod
    def normalize(cls, val):
        return AngleBase.normalize_to(val, (- math.pi, math.pi), 2 * math.pi)

    def __add__(self, other):
        if isinstance(other, AngleDiff):
            return AngleDiff(rad=self.rad + other.rad)
        elif isinstance(other, Angle):
            return Angle(rad=self.rad + other.rad)
        elif isinstance(other, Number):
            return Angle(rad=self.rad + other)
        else:
            raise NotImplementedError()
