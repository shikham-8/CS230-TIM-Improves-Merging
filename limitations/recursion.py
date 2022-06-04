# Recursion example

from math import floor, sqrt, log10

# fibonacci test


def fib(x: int) -> int:
    if (int(x) <= 1):
        return 1
    return fib(x-1) + fib(x-2)


def fib2(y: float) -> int:
    y = floor(y)
    if (y == 1):
        return 1
    if (y <= 0):
        return 1
    return fib2(y-2) + fib2(y-1)


# run: crosshair cover recursion.<functionName>
