class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            # Only consider numbers with an even number of digits.
            if len(s) % 2 != 0:
                continue
            
            mid = len(s) // 2
            first_half = s[:mid]
            second_half = s[mid:]
            
            # Calculate the sum of digits in both halves.
            if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in  second_half):
                count += 1
        
        return count