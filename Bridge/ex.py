from abc import ABC, abstractmethod


class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'drawing pixels a circle of radius {radius}')


class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, radius, renderer: Renderer):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(5, raster)
    circle.draw()
    circle.resize(2)
    circle.draw()
