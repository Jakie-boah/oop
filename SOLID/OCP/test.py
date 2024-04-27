from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(
            map(
                lambda spec: spec.is_satisfied(item), self.args
            )
        )


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpec(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class BetterFilter(Filter):
    def filter(self, items, spec):
        for p in items:
            if spec.is_satisfied(p):
                yield p



