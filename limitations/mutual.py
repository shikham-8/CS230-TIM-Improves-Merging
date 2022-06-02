def foo(x: int):
    if (x == 0):
       return 0
    return 1 + bar(x-1)

def bar(x: int):
    if (x == 0):
       return 0
    return 1 + foo(x-1)
