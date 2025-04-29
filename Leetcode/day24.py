from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_distinct = len(set(nums))
        freq = defaultdict(int)
        distinct_in_window = 0
        ans = 0
        
        right = 0
        for left in range(n):
            while right < n and distinct_in_window < total_distinct:
                if freq[nums[right]] == 0:
                    distinct_in_window += 1
                freq[nums[right]] += 1
                right += 1
            if distinct_in_window == total_distinct:
                ans += (n - right + 1)
            else:
                break
        
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                distinct_in_window -= 1
        
        return ans