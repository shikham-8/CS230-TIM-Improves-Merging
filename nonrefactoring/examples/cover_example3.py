from typing import List

# run: crosshair cover cover_example.test

def test00(a: List[int]) -> None:
    if not a:
        print("empty")
    elif a[0] == 1:
        print("starts with 1")
    else:
        print("doesn't start with 1")

def test02(a: List[int]) -> None:
    if not a:
        print("empty")
    elif a[0] == 1:
        print("starts with 1")
    else:
        print("doesn't start with 1")