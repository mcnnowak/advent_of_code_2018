#!/bin/python

class Rectangle(object):
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x, self.y = x, y
        self.w, self.h = w, h

    def intersect(self, other):
        x_max = min(self.x + self.w, other.x + other.w)
        x_min = max(self.x, other.x)

        if x_min > x_max:
            return None

        y_max = min(self.y + self.h, other.y + other.h)
        y_min = max(self.y, other.y)

        if y_min > y_max:
            return None

        return Rectangle(x_min, y_min, x_max - x_min, y_max - y_min)

    def __repr__(self):
        return '<Rectangle x={} y={} w={} h={}>'.format(self.x, self.y, self.w, self.h)

if __name__ == '__main__':
    r1, r2 = Rectangle(0, 0, 2, 2), Rectangle(1, 1, 1, 1)

    print('Should intersect:', r1, r2)
    print(r1.intersect(r2))

    r3 = Rectangle(3, 3, 2, 2)

    print('Shouldn\'t intersect:', r1, r3)
    print(r1.intersect(r3))
