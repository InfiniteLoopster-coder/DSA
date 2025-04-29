class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9+7

        children = [[] for _ in range(maxValue+1)]
        for v in range(1, maxValue+1):
            for u in range(v+v, maxValue+1, v):
                children[v].append(u)
        fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % MOD
        invfact = [1]*(n+1)
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i]*i % MOD
        
        def comb(a: int, b: int) -> int:
            if b<0 or b> a: 
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a-b] % MOD
        
        import math
        Kmax = math.floor(math.log2(maxValue)) + 1
        

        g_prev = [0]*(maxValue+1)
        g_curr = [0]*(maxValue+1)
        
        for v in range(1, maxValue+1):
            g_prev[v] = 1
        
        answer = 0
        
        for k in range(1, Kmax+1):
            c = comb(n-1, k-1)
            total_chains = sum(g_prev[1:]) % MOD
            answer = (answer + total_chains * c) % MOD
            
            for v in range(1, maxValue+1):
                s = 0
                for u in children[v]:
                    s += g_prev[u]
                    if s >= MOD:
                        s -= MOD
                g_curr[v] = s
            
 
            g_prev, g_curr = g_curr, g_prev
        
        return answer