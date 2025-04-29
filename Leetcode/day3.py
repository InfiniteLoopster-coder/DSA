from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max  = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        suffix_max = [0] * n
        suffix_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        
        max_triplet_value = float('-inf')

        for j in range(1, n - 1):
            current_value = (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1]
            max_triplet_value = max(max_triplet_value, current_value)
        return max_triplet_value if max_triplet_value > 0 else 0

