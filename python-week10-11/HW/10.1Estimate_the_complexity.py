# (a)
def has_pair_summing(xs, target):
    """True if any two elements of xs add up to target."""
    seen = set()

    for x in xs:
        if target - x in seen:
            return True
        seen.add(x)

    return False


# (b)
def lookup_all(ids, records):
    """Fetch every record named in `ids` from the `records` dictionary."""
    out = []

    for i in ids:
        if i in list(records.keys()):
            out.append(records[i])

    return out


# (c)
def first_repeat(xs):
    """Return the first repeated value while scanning from left to right."""
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return xs[i]

    return None


# (d)
def median_per_group(groups):
    """Return the median for each group of values."""
    out = {}

    for name, values in groups.items():
        sorted_values = sorted(values)
        n = len(sorted_values)

        if n % 2 == 1:
            out[name] = sorted_values[n // 2]
        else:
            out[name] = (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2

    return out

# (e)
def count_duplicate_pairs(xs):
    n = 0
    for i, a in enumerate(xs):
        for b in xs[i + 1:]:
            if a == b:
                n += 1
    return n


# ANSWERS:
# a = O(n)
# a    seen = set()
#    for x in xs:
#        if target - x in seen:

# b = O(n^2)
# b     for i in ids:
#            if i in list(records.keys()):


# c = O(n^2)
# c     for i in range(len(xs)):
#           for j in range(i + 1, len(xs)):

# d = O(n log n)
# d
#    for name, values in groups.items():
#        sorted_values = sorted(values)

# e = O(n^2)
# e for b in xs[i + 1:]:
