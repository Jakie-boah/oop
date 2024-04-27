import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds')
        return result

    return wrapper


@time_it
def some_op():
    print('start')
    time.sleep(2)
    return 123


if __name__ == '__main__':
    some_op()
