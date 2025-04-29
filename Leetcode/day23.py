from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = [0] * 46
        ds = [0] * (n + 1)
        for i in range(1, n + 1):
            ds_i = ds[i // 10] + (i % 10)
            ds[i] = ds_i
            counts[ds_i] += 1
        max_size = max(counts)
        return counts.count(max_size)