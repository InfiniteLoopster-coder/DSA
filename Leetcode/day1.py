from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            # Determine the next question index after solving the current one
            next_index = i + brainpower + 1
            # If next_index is within bounds, add dp[next_index]; otherwise, just use points
            solve = points + (dp[next_index] if next_index < n else 0)
            # Option to skip the current question
            skip = dp[i + 1]
            # Choose the option that gives the maximum points
            dp[i] = max(solve, skip)
        
        return dp[0]

        