try:
    n = int(input("number: "))
except ValueError:
    print("not a number")
else:
    print(f"got: {n}")