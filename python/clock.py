import time


def clock(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print(func.__name__ + '() Take {} sec.'.format(t1-t0))
        return result
    return wrapper

