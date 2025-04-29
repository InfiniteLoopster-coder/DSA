class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count_k_up_to(X: int, k: int, limit: int) -> int:
            sX = str(X)
            if len(sX) < k:
                return 0
            if len(sX) > k:
                return limit * ((limit + 1) ** (k - 1))
            

            digits = list(map(int, sX))
            
            @lru_cache(maxsize=None)
            def dp(pos: int, tight: bool) -> int:
                if pos == k:
                    return 1
                res = 0
                low = 1 if pos == 0 else 0
                high = digits[pos] if tight else limit
                for d in range(low, limit + 1):
                    if d > high:
                        break
                    new_tight = tight and (d == high)
                    res += dp(pos + 1, new_tight)
                return res
            
            return dp(0, True)
        

        def count_range(k: int, A: int, B: int, limit: int) -> int:
            if A > B:
                return 0
            return count_k_up_to(B, k, limit) - count_k_up_to(A - 1, k, limit)
        

        N = int(s)
        L = len(s)
        total = 0
        
        if start <= N <= finish:
            total += 1
        
        d_max = len(str(finish))
        k_max = max(0, d_max - L) 
        
        power = 10 ** L  
        

        for k in range(1, k_max + 1):
            if finish < N:
                continue
            

            if start > N:
                candidate_lower = (start - N + power - 1) // power  
            else:
                candidate_lower = 0
            
            candidate_upper = (finish - N) // power
        
            lower_valid = 10 ** (k - 1)              
            upper_valid = int(str(limit) * k)        
            
            effective_lower = max(lower_valid, candidate_lower)
            effective_upper = min(upper_valid, candidate_upper)
            
            if effective_lower <= effective_upper:
                cnt = count_range(k, effective_lower, effective_upper, limit)
                total += cnt
        
        return total