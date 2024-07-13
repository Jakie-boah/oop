class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self._name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'


if __name__ == '__main__':
    drawin = GraphicObject()
    drawin._name = 'My Drawing'
    drawin.children.append(Square('red'))
    drawin.children.append(Square('yellow'))

    group = GraphicObject()
    group.children.append(Circle('blue'))
    group.children.append(Square('blue'))
    drawin.children.append(group)

    print(drawin)
