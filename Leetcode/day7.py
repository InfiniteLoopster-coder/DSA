from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        # If total is odd, can't split evenly
        if S % 2 == 1:
            return False

        target = S // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Traverse backwards so each num is used once
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True

        return dp[target]