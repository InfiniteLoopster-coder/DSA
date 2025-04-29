from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        pairs = 0  
        ans = 0
        left = 0
        for right in range(n):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1
            while pairs >= k and left <= right:
                ans += (n - right)
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
        return ans