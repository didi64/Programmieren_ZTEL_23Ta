import math


class Vec2d(tuple):
    """A 2 dimensional vector class.
       Derived from tuple, so a vector is a tuple!
       Provides vector addition and multipliation with a scaler
       Vec2d(1, 2) + Vec2d(3, 4) == Vec2d(4, 6)
       Vec2d(1, 2) * 2 == Vec2d(2, 4)
    """
    import math
    DEGREE = 180 / math.pi

    @staticmethod
    def sign(x):
        '''returns 1 if x > 0, -1 if x < 0, and 0 if x == 0'''
        return (x > 0) - (x < 0)

    @classmethod
    def from_polar(cls, r, arg, degree=True):
        '''creates a vector from polar coordinats'''
        arg = arg/Vec2d.DEGREE if degree else arg
        return cls(r*math.cos(arg), r*math.sin(arg))

    @classmethod
    def bbox(cls, pts=(), lines=()):
        '''returns a tuple (lower_left:Vec2d, width:float, height:float)'''
        assert not pts or isinstance(pts[0], tuple), 'pts is not a list of tuples!'
        assert not lines or not lines[0] or isinstance(lines[0][0], tuple), \
            'lines is not a list of lists of tuples!'

        xs = [pt[0] for pt in pts] + [pt[0] for line in lines for pt in line]
        ys = [pt[1] for pt in pts] + [pt[1] for line in lines for pt in line]
        lower_left = cls(min(xs), min(ys))
        upper_right = cls(max(xs), max(ys))
        dims = upper_right-lower_left
        bbox = (lower_left, *dims)
        return bbox

    @classmethod
    def bbox2rect(cls, bbox):
        '''returns the 4 corners of the bbox as vectors
           first corner is the lower left, enumerates corners counterclockwise
        '''
        rect = [bbox[0],
                bbox[0] + cls(bbox[1], 0),
                bbox[0] + cls(bbox[1], bbox[2]),
                bbox[0] + cls(0, bbox[2]),
                ]
        return rect

    def __new__(cls, x, y):
        assert isinstance(x, (int, float, complex)) and isinstance(y, (int, float, complex)),\
               'Vector components must be of type int, float or complex!'
        return tuple.__new__(cls, (x, y))

    def __add__(self, other):
        return Vec2d(self[0] + other[0], self[1] + other[1])   

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec2d(self[0] * other, self[1] * other)
        raise NotImplementedError

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (1/other)

    def __neg__(self):
        return (-1) * self

    def __sub__(self, other):
        return self + -other

    def lerp(self, other, t):
        '''returns self+t(other-self)'''
        return (1-t)*self + t*other

    def norm(self):
        '''returns the length of the vector'''
        x, y = self
        return math.sqrt(x ** 2 + y ** 2 )

    def hat(self):
        '''returns self/self.norm()'''
        return self / self.norm()

    def perp(self):
        '''rotates the vector by 90 degree counterclockwise'''
        return Vec2d(-self[1], self[0])

    def rotate(self, alpha, degree=True):
        '''rotates the vector counterclockwise'''
        factor = Vec2d.DEGREE if degree else 1
        alpha = alpha/factor
        c = math.cos(alpha)
        s = math.sin(alpha)
        return Vec2d(c*self[0] - s*self[1], s*self[0] + c*self[1])                  

    def dot(self, other):
        '''returns the dot/scalar product'''
        return self[0]*other[0] + self[1]*other[1]

    def area(self, other):
        '''returns the area of the spanned parallelogram'''
        return self[0]*other[1] - self[1]*other[0]

    def angle(self, other, degree=True):
        '''returns the signed angle'''
        factor = Vec2d.DEGREE if degree else 1
        area = self.area(other)
        cos = self.dot(other)/self.norm()/other.norm()
        return Vec2d.sign(area)*factor*math.acos(cos)

    def arg(self, degree=True):
        '''returns the argument of the vector'''
        x, y = self
        factor = Vec2d.DEGREE if degree else 1
        return math.atan2(y, x) * factor

    def scale(self, x, y=None):
        '''scale x- and y-coordinates'''
        y = x if y is None else y
        return Vec2d(x*self[0], y*self[1])

    def xmirror(self):
        '''mirror at x-axis'''
        return Vec2d(-self[0], self[1])

    def ymirror(self):
        '''mirror at y-axis'''
        return Vec2d(self[0], -self[1])

    def as_polar(self):
        '''returns vector in polar form'''
        return (self.norm(), self.arg())

    def __repr__(self):
        return 'Vec2d({}, {})'.format(*self)