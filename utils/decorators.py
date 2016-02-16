from functools import wraps
import time


def time_this(function_to_time):
    """
    decorator used to time functions
    """
    @wraps(function_to_time)
    def timer(*args, **kwargs):
        start = time.time()
        result = function_to_time(*args, **kwargs)
        end = time.time()
        print("%s (%s, %s) %.4f sec" % (function_to_time.__name__, args, kwargs, end-start))
        return result

    return timer


@time_this
def make_list_comprehension(size):
    import random

    comprehension = [random.randint(1, 100) for _ in range(size)]
    return comprehension


@time_this
def make_list_for_loop(size):
    import random

    for_loop = []
    for _ in range(size):
        for_loop.append(random.randint(1, 100))

make_list_comprehension(1000000)
make_list_for_loop(1000000)
