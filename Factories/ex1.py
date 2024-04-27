from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'put in tea bag, boil water, '
              f' pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, '
              f' pour {amount}ml, enjoy!')
        return Coffee()


def make_drink(type_):
    if type_ == 'tea':
        return TeaFactory().prepare(200)
    elif type_ == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                print(d)
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                print(factory_name)
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('available')
        for f in self.factories:
            print(f[0])

        s = input(f'pick a drink (0-{len(self.factories) - 1}) ')
        idx = int(s)
        s = input('specify amount ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    dm = HotDrinkMachine()
    dm.make_drink()
