def rep_cat(x, y):
    return str(x) * 10 + str(y) * 5


print(rep_cat(2, 3))


def factorial(n) -> int:
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def print_num_type():
    for i in range(0, 20, 3):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")


print_num_type()
