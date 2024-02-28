def adder(x, y):
    if y == 1:
        return x + 1
    else:
        return 1 + adder(x, y - 1)


print(adder(2, 4))
