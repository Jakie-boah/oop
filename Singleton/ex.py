import random


class Database:
    _instance = None

    def __init__(self):
        id_ = random.randint(1, 101)
        print('id = ', id_)
        print('loading db')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loadin db')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
    