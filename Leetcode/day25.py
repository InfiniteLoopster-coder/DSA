from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        A = [1 if x % modulo == k else 0 for x in nums]

        prefix_mod = 0
        count = defaultdict(int)

        count[0] = 1
        ans = 0
        for a in A:
            prefix_mod = (prefix_mod + a) % modulo
            target = (prefix_mod - k) % modulo
            ans += count[target]
            count[prefix_mod] += 1
        return ans