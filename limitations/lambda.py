from typing import Any, Dict, List, Optional, Tuple, Generator, Callable, Iterable, IO, TypeVar, Mapping


def lambdaFn(a: Callable[[int], int]):
    if a:
        return a(2) + 4
    else:
        return "hello"


# print(lambdaFn(lambda a: a*a))
# print(lambdaFn(None))

# run: crosshair cover lambda.<functionName>
