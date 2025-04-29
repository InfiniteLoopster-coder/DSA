from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_or = 0
        for num in nums:
            total_or |= num  # Compute the bitwise OR of all numbers.
        # Multiply by 2^(n-1) to get the sum of XOR totals.
        return total_or * (1 << (len(nums) - 1))