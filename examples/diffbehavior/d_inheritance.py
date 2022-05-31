import dataclasses
@dataclasses.dataclass
class Obj:
    num: int
    def __init__(self, x):
        self.num = x
    def action(self):
        self.num+=2
@dataclasses.dataclass
class Sub(Obj):
    def __init__(self, x):
        self.num = x
    def action(self):
        self.num+=3

def o(a: Obj):
    a.action()
    return a.num

def s(a: Sub):
    a.action()
    return a.num
