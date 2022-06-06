from typing import List


def increment_list(a: List[int]) -> List[int]:
    i = 0
    j = 0
    while i < len(a) - 1:
        a[i] += 1
        i += 1
    return a
