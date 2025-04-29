from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1
        distinct_values = set(nums)
        operations = sum(1 for num in distinct_values if num > k)
        return operations