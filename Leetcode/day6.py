from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1]*n
        prev = [-1]*n

        best_len, best_end = 1, 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > best_len:
                best_len, best_end = dp[i], i

        # Reconstruct
        res = []
        cur = best_end
        while cur != -1:
            res.append(nums[cur])
            cur = prev[cur]
        return res[::-1]