from typing import List

# run: crosshair diffbehavior a.increment_list b.increment_list_refactored

def increment_list_refactored(a: List[int]) -> None:
  for i in range(len(a)):
    a[i] += 1