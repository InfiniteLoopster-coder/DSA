from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        M = max(nums)
        n = len(nums)

        ans = 0
        left = 0
        curr = 0 

        for right, x in enumerate(nums):
            curr += (1 if x == M else 0)

            while left <= right and curr >= k:
                curr -= (1 if nums[left] == M else 0)
                left += 1

            ans += left

        return ans