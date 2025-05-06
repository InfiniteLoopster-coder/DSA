class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        f = [0]*(n+1)
        p = [0]*(n+1)

        f[0], f[1] = 1, 1
        p[0], p[1] = 0, 0

        for i in range(2, n+1):
            f[i] = (f[i-1] + f[i-2] + 2*p[i-1]) % MOD
            p[i] = (p[i-1] + f[i-2]) % MOD

        return f[n]