from collections import Counter
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = Counter()
        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            freq[key] += 1
        ans = 0
        for f in freq.values():
            if f > 1:
                ans += f * (f - 1) // 2
        return ans