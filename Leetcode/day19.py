from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
    
        def count_leq(limit: int) -> int:
            cnt = 0
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s <= limit:
                    cnt += (r - l)
                    l += 1
                else:
                    r -= 1
            return cnt

        return count_leq(upper) - count_leq(lower - 1)