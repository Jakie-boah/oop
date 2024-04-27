from abc import ABC, abstractmethod


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'a circle with {self.radius} radius and {self.radius * 2} area'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'a square with {self.side} side and {self.side ** 2} area'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception('Cannot apply same decorator')

        self.color = color
        self.shape = shape

    def __str__(self):
        return f'{self.shape} {self.color}'


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100}% transparency'


if __name__ == '__main__':
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, 'red')
    print(red_circle)
    red_half_transparent_circle = TransparentShape(
        red_circle, 0.5
    )
    print(red_half_transparent_circle)
    mixed = ColoredShape(ColoredShape(Square(3), 'red'), 'green')
