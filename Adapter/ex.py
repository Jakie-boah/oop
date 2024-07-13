class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(point):
    print('.', end='')


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter:
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        super().__init__()
        # логика рисования
        self.cache[self.h] = 'точки после рисования'

    def __iter__(self):
        return iter(self.cache[self.h])

    
def draw(rcs):
    print('\n\n--- Drawing')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6),
    ]
