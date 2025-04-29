class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Precompute factorials up to n
        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i

        seen = set()
        result = 0

        # Determine the range for generating half of the palindrome
        half_len = (n + 1) // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len

        for half in range(start, end):
            half_str = str(half)
            # Construct the full palindrome
            if n % 2 == 0:
                full_str = half_str + half_str[::-1]
            else:
                full_str = half_str + half_str[-2::-1]

            full_num = int(full_str)

            # Check if the palindrome is divisible by k
            if full_num % k != 0:
                continue

            # Sort the digits to create a unique signature
            sorted_digits = ''.join(sorted(full_str))
            if sorted_digits in seen:
                continue
            seen.add(sorted_digits)

            # Count the frequency of each digit
            digit_count = Counter(full_str)

            # Calculate the number of unique permutations without leading zeros
            total_permutations = 0
            for first_digit in range(1, 10):
                if digit_count[str(first_digit)] == 0:
                    continue
                digit_count[str(first_digit)] -= 1
                perms = fac[n - 1]
                for count in digit_count.values():
                    perms //= fac[count]
                total_permutations += perms
                digit_count[str(first_digit)] += 1

            result += total_permutations

        return result