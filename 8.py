import time

s1 = []
s2 = []


def tictoc(func):
    def wrapper(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        runtime = t2 - t1
        # print(f"Function {func.__name__} took {runtime} seconds to execute")
        # print("-" * 100)

        if func.__name__ == "fibonacci_with_for":
            s1.append(runtime)
        elif func.__name__ == "fibonacci_with_while":
            s2.append(runtime)

    return wrapper


@tictoc
def fibonacci_with_for(n):
    a, b = 0, 1
    fib_list = []

    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b

    # print(fib_list)


@tictoc
def fibonacci_with_while(n):
    a, b = 0, 1
    fib_list = []

    while len(fib_list) != n:
        fib_list.append(a)
        a, b = b, a + b

    # print(fib_list)


for i in range(30):
    fibonacci_with_for(50000)
    fibonacci_with_while(50000)

print(s1)
print(sum(s1) / len(s1))
print(s2)
print(sum(s2) / len(s2))
