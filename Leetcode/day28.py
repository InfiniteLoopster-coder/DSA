from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l = 0
        r = -1
        curr_sum = 0
        curr_len = 0
        for l in range(n):
            if r < l - 1:
                r = l - 1
                curr_sum = 0
                curr_len = 0
            while r + 1 < n and (curr_sum + nums[r + 1]) * (curr_len + 1) < k:
                r += 1
                curr_sum += nums[r]
                curr_len += 1
            ans += (r - l + 1)
            if r >= l:
                curr_sum -= nums[l]
                curr_len -= 1
        return ans