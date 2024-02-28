def multiply(x, y):
    if y == 1:
        return x
    else:
        return x + multiply(x, y - 1)


print(multiply(3, 5))
