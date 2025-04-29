class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)  # 1-indexed
    
    def update(self, index: int, delta: int) -> None:
        # index is expected to be 1-indexed.
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index: int) -> int:
        # Returns the cumulative sum from 1 up to index (inclusive)
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & -index
        return s


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n
        for i, val in enumerate(nums2):
            pos2[val] = i
        

        A = [0] * n
        for i in range(n):
            A[i] = pos2[nums1[i]]

        L = [0] * n
        R = [0] * n


        BIT_left = FenwickTree(n)
        for j in range(n):
            L[j] = BIT_left.query(A[j])  
            BIT_left.update(A[j] + 1, 1)
        

        BIT_right = FenwickTree(n)
        for j in range(n - 1, -1, -1):
            R[j] = BIT_right.query(n) - BIT_right.query(A[j] + 1)
            BIT_right.update(A[j] + 1, 1)
        

        total = 0
        for j in range(n):
            total += L[j] * R[j]
        
        return total