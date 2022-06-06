from typing import List


def increment_list(a: List[int]) -> None:
    for i in range(len(a)):
        a[i] += 1
