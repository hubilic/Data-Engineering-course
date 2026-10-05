from contextlib import contextmanager
import time
from unicodedata import name

@contextmanager
def timer(name):
    start_time = time.perf_counter()
    try:
        yield
    finally:
        elapsed_time = time.perf_counter() - start_time
    print(f"{name} took {elapsed_time * 1000:.1f} ms")