import time

def measure(fn, *args):
    t0 = time.perf_counter()
    out = fn(*args)
    return out, time.perf_counter() - t0





def squares_of_multiples(n):
    out = []
    for i in range(n):
        if i % 3 == 0:
            out = out + [i * i]
    return out

#ANSWERS:
# a = O(n^2)
#out.append(x) dodaje element do istniejacej listy (czyli jest O(1))
# out = out + [x] tworzy nowa liste i kopiuje dotychasowe elementy


def squares_of_multiples_fast(n):
    out = []
    for i in range(n):
        if i % 3 == 0:
            out.append(i * i)
    return out


assert squares_of_multiples_fast(120_000) == squares_of_multiples(120_000)

original_result, original_time = measure(squares_of_multiples, 120_000)

fast_result, fast_time = measure(squares_of_multiples_fast, 120_000)

print(f"HW: {original_time:.4f} s")
print(f"Fast:{fast_time:.4f} s")
print(f"Fastest {original_time / fast_time:.1f}x")
