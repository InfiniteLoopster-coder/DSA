from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if 2 * (a + c) == b:
                count += 1
        return count
        