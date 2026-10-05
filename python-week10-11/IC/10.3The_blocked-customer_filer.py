import time

def measure(fn, *args):
    t0 = time.perf_counter()
    out = fn(*args)
    return out, time.perf_counter() - t0




import random


random.seed(42)

orders = [
    {"id": i, "customer_id": random.randint(1, 50_000)}
    for i in range(1, 60_001)
]
blocked = [random.randint(1, 50_000) for _ in range(4_000)]

def active_orders(orders, blocked):
    out = []

    for o in orders:
        if o["customer_id"] not in blocked:
            out.append(o)

    return out


# ANSWERS:
# a = O(n^2)


def active_orders_fast(orders, blocked):
    blocked_set = set(blocked)
    out = []

    for o in orders:
        if o["customer_id"] not in blocked_set:
            out.append(o)

    return out


assert active_orders_fast(orders, blocked) == active_orders(orders, blocked)

original_result, original_time = measure(active_orders, orders, blocked)

fast_result, fast_time = measure(active_orders_fast, orders, blocked)

print(f"IC:{original_time:.4f} s")
print(f"Fast:{fast_time:.4f} s")
print(f"Fastest:{original_time / fast_time:.1f}x")
