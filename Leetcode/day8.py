from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_elements = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in unique_elements:
                return (i // 3) + 1
            unique_elements.add(nums[i])
        return 0