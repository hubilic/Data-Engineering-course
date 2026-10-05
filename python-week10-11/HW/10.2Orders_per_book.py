import time

def measure(fn, *args):
    t0 = time.perf_counter()
    out = fn(*args)
    return out, time.perf_counter() - t0



import random
random.seed(11)
orders = [{"id": i, "book_id": random.randint(1, 800)} for i in
range(1, 40_001)]



def orders_per_book(orders):
    book_ids = []
    for o in orders:
        if o["book_id"] not in book_ids:
            book_ids.append(o["book_id"])

    counts = {}
    for b in book_ids:
        n = 0
        for o in orders:
            if o["book_id"] == b:
                n += 1
        counts[b] = n
    return counts

#ANSWERS:
# a = O(n^2)


def orders_per_book_fast(orders):
    counts = {}
    for o in orders:
        book_id = o["book_id"]
        counts[book_id] = counts.get(book_id, 0) + 1
    return counts

assert orders_per_book_fast(orders) == orders_per_book(orders)

original_result, original_time = measure(orders_per_book, orders)

fast_result, fast_time = measure(orders_per_book_fast, orders)

print(f"HW: {original_time:.4f} s")
print(f"Fast:{fast_time:.4f} s")
print(f"Fastest:{original_time / fast_time:.1f}x")