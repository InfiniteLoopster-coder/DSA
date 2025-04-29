from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_invalid = -1      
        last_min = -1         
        last_max = -1          
        answer = 0

        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                last_invalid = i
            if x == minK:
                last_min = i
            if x == maxK:
                last_max = i
            valid_starts = min(last_min, last_max) - last_invalid
            if valid_starts > 0:
                answer += valid_starts
        return answer