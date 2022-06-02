from typing import List, Optional
def average(nums: List[float], default:Optional[float] = None) -> float:
    if len(nums) == 0:
        if default is None:
            print("FAULT")
            return -1
        return default
    return sum(nums) / len(nums)
