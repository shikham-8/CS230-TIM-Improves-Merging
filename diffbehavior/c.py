from typing import List

# run: crosshair diffbehavior a.increment_list c.increment_list_refactored_wrong

def increment_list_refactored_wrong(a: List[int]) -> None:
    i = 0
    while i < len(a) - 1:
        a[i] += 1
        i += 1