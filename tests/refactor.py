from typing import List


def increment_list(a: List[int]) -> None:
    i = 0
    while i < len(a) - 1:
        a[i] += 1
        i += 1
