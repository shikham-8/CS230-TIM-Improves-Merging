from typing import List

def increment_list_refactored(a: List[int]) -> None:
  for i in range(len(a)):
    a[i] += 1