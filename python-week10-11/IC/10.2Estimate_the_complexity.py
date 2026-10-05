# (a)
# def unique_pairs(xs):
#     """Every unordered pair: [1, 2, 3] -> (1, 2), (1, 3), (2, 3)."""
#     out = []
#     for i in range(len(xs)):
#         for j in range(i + 1, len(xs)):
#             out.append((xs[i], xs[j]))
#     return out

# (b)
# def common(a, b):
#     """Elements of list `a` that also appear in list `b`."""
#     out = []
#     for x in a:
#         if x in b:
#             out.append(x)
#     return out

# (c)
# def top_earner(employees):
#     """Return the single employee with the highest salary."""
#     return sorted(employees, key=lambda e: e["salary"])[-1]

# (d)
# def chunks(xs, size):
#     """Split a list into consecutive blocks of `size`."""
#     out = []
#     i = 0
#     while i < len(xs):
#         out.append(xs[i : i + size])
#         i += size
#     return out

# ANSWERS:
# a = O(n^2)
# for j in range(i + 1, len(xs)):

# b = O(n^2)
# if x in b:

# c = O(n log n)
# return sorted(employees, key=lambda e: e["salary"])[-1]

# d = O(n)
# out.append(xs[i : i + size])
