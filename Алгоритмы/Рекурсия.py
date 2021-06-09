def factorial_r(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_r(n - 1)


def factorial_c(n):
    accumulator = 1
    i = n
    while i > 1:
        accumulator *= i
        i -= 1
    return accumulator


print(factorial_r(100))
print(factorial_c(100))
