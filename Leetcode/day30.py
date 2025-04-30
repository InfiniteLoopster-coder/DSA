import math
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            digit_len = int(math.log10(x)) + 1
        
            if digit_len % 2 == 0:
                count += 1

        return count
