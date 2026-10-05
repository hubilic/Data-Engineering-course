import time

def measure(fn, *args):
    t0 = time.perf_counter()
    out = fn(*args)
    return out, time.perf_counter() - t0




import random
random.seed(5)
events = [{"player": f"p{i}", "score": random.randint(0,
1_000_000)} for i in range(1, 8_001)]




def top5(events):
    board = []
    for e in events:
        board.append(e)
        board.sort(key=lambda x: -x["score"])
    return [e["player"] for e in board[:5]]


def top5_fast(events):
    board = []
    for e in events:
        board.append(e)
        if len(board) > 5:
            board.sort(key=lambda x: -x["score"])
            board.pop()

    board.sort(key=lambda x: -x["score"])

    return [e["player"] for e in board]


assert top5_fast(events) == top5(events)

original_result, original_time = measure(top5, events)

fast_result, fast_time = measure(top5_fast, events)

print(f"HW: {original_time:.4f} s")
print(f"Fast:{fast_time:.4f} s")
print(f"Fastest {original_time / fast_time:.1f}x")