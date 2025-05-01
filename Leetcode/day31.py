from typing import List
import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        def can_do(k: int) -> bool:
            T = tasks[:k]
            W = workers[m-k:].copy()
            rem = pills
            for t in reversed(T):
                if W and W[-1] >= t:
                    W.pop()
                else:
                    if rem == 0:
                        return False
                    need = t - strength
                    idx = bisect.bisect_left(W, need)
                    if idx == len(W):
                        return False
                    W.pop(idx)
                    rem -= 1
            return True

        left, right, ans = 0, min(n, m), 0
        while left <= right:
            mid = (left + right) // 2
            if can_do(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
            