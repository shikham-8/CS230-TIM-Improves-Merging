import dataclasses
import obj

@dataclasses.dataclass
class A(obj.Obj):
  def __init__(self, x):
    self.num = x
  def action(self):
    self.num += 3

def foo(x: obj.Obj):
  x.action()
  return x.num
'''
def bar(x: A):
  x.action()
  return x.num
'''
