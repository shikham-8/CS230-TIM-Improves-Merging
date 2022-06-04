from math import floor, sqrt, log10
from typing import Any, Dict, List, Optional, Tuple, Generator, Callable, Iterable, IO, TypeVar, Mapping


def apiTest(a: float) -> float:
    # simple API call
    return sqrt(a)


def apiTest2(a: Dict[float, float]) -> List[float]:
    l = []
    for key in a.keys():
        l.append(log10(a[key]))
    return l

# run: crosshair cover apiCalls.<functionName>
