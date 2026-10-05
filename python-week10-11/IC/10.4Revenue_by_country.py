import time

def measure(fn, *args):
    t0 = time.perf_counter()
    out = fn(*args)
    return out, time.perf_counter() - t0



import random


random.seed(7)

COUNTRIES = ["PL", "DE", "GB", "CZ", "FR", "ES", "US"]
customers = [
    {"id": i, "country": random.choice(COUNTRIES)}
    for i in range(1, 5_001)
]
orders = [
    {
        "id": i,
        "customer_id": random.randint(1, 5_000),
        "amount": random.randrange(1990, 9991) / 100,
    }
    for i in range(1, 25_001)
]

def revenue_by_country(orders, customers):
    totals = {}

    for o in orders:
        for c in customers:
            if c["id"] == o["customer_id"]:
                totals[c["country"]] = totals.get(c["country"], 0) + o["amount"]
                break

    return {k: round(v, 2) for k, v in totals.items()}


# ANSWERS:
# a = O(n^2)


def revenue_by_country_fast(orders, customers):
    customer_country = {}

    for c in customers:
        customer_country[c["id"]] = c["country"]

    totals = {}

    for o in orders:
        country = customer_country[o["customer_id"]]
        totals[country] = totals.get(country, 0) + o["amount"]

    return {k: round(v, 2) for k, v in totals.items()}


assert revenue_by_country_fast(orders, customers) == revenue_by_country(
    orders, customers
)

original_result, original_time = measure(revenue_by_country, orders, customers)

fast_result, fast_time = measure(revenue_by_country_fast, orders, customers)


print(f"IC: {original_time:.4f} s")
print(f"Fast:{fast_time:.4f} s")
print(f"Fastest:{original_time / fast_time:.1f}x")
