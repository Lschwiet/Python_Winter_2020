class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

    def calc_perimeter(self):
        return 2 * self._a + 2 * self.b

class Square(Rectangle):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, a)
        #self._a = a

import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))

    def cal_perimeter(self):
        return 2 * math.pi * self._a

class Triangle(Shape):

    def calc_surface(self):
        return self._a*self.b/2

    def calc_perimeter(self):
        return

    def __repr__(self):
        return self.__class__.__name__ + " [Width = " + str(self._a) + ",Height = " + str(self.b) + "] at " + str(hex(id(self)))

class EquilateralTriangle(Shape):
    def __init__(self, a):
        super().__init__(a, 0)

    def calc_surface(self):
        return 0.25 * self._a**2 * math.sqrt(3)

    def calc_perimeter(selfs):
        return 3 * self._a

    def __repr__(self):
        return self.__class__.__name__ + " [sidelength = " + str(self._a) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)
print(r)
#r._a = 600
print(r.calc_surface())
r.swap_sides()
print(r)

c = Circle(7)
print(c)
print(c.calc_surface())

t = Triangle(3, 3)
print(t)
print(t.calc_surface())

et = EquilateralTriangle(2)
print(et.calc_surface())

s = Square(3)
print(s.calc_surface())
print(s.calc_perimeter())