from typing import List
import math
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0

        for x, cnt in freq.items():
            group_size = x + 1
            # number of full groups needed
            num_groups = math.ceil(cnt / group_size)
            total += num_groups * group_size

        return total