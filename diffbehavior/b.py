from typing import List

def cut2(a: List[int], i: int) -> None:
  a[:] = a[:i] + a[i+1:]
