from typing import List


def increment_list(a: List[int]) -> None:
    a_length = len(a)
    for i in range(a_length):
        a.append(a[i] + 1)
    for i in range(a_length):
        a.pop(0)
