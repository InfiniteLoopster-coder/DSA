class Solution:
    def countAndSay(self, n: int) -> str:
        def run_length_encode(s: str) -> str:
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)

        term = "1"
        for _ in range(n - 1):
            term = run_length_encode(term)
        return term
