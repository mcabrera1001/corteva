from functools import wraps
import time
import logging


def time_process(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        logging.info(f"Process {func.__name__}{args} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper
