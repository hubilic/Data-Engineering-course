# (a) for x in xs: print(x)
# (b) for x in xs:
#         for y in xs: print(x, y)
# (c) xs[0]
# (d) xs[len(xs) // 2]
# (e) "apple" in {"apple", "banana"}
# (f) "apple" in ["apple", "banana"]
# (g) sorted(xs)
# (h) min(xs)
# (i) for x in xs: bisect.insort(sorted_list, x)
# (j) for x in xs: sorted_list.append(x); sorted_list.sort()

# ANSWERS:
# a = O(n)
# b = O(n^2)
# c = O(1)
# d = O(1)
# e = O(1)
# f = O(n)
# g = O(n log n)
# h = O(n)
# i = O(n log n)
# j = O(n log n)
