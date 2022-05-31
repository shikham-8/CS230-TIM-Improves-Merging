import dataclasses
@dataclasses.dataclass
class Obj:
  num: int
  def __init__(self, x):
    num = x
  def action(self):
    self.num += 2
