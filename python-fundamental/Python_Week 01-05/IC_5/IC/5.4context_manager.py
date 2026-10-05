class Timer:
    def __init__(self, name: str):
        self.name = name
        self.start_time = None

    def __enter__(self):
        import time
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        elapsed_time = time.perf_counter() - self.start_time
        print(f"{self.name} took {elapsed_time * 1000:.1f} ms")
        return False