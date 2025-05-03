class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        res = list(dominoes)
        prev_force, prev_i = 'L', -1
        for i in range(n + 1):
            curr = dominoes[i] if i < n else 'R'
            if curr == '.':
                continue
            if prev_force == curr:
                for j in range(prev_i + 1, i):
                    res[j] = curr

            elif prev_force == 'R' and curr == 'L':
                l, r = prev_i + 1, i - 1
                while l < r:
                    res[l] = 'R'
                    res[r] = 'L'
                    l += 1
                    r -= 1

            prev_force, prev_i = curr, i

        return "".join(res)