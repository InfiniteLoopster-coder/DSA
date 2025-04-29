from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_pref = 0
        max_pref = 0

        # Build prefix sums and record their min/max
        for d in differences:
            prefix += d
            min_pref = min(min_pref, prefix)
            max_pref = max(max_pref, prefix)
        count = (upper - max_pref) - (lower - min_pref) + 1
        return max(0, count)
    
    