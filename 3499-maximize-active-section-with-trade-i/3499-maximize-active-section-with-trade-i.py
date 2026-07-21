class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')

        prev_zero = -10**9
        best = 0

        i = 0
        n = len(s)

        while i < n:
            j = i

            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '0':
                best = max(best, prev_zero + length)
                prev_zero = length

            i = j

        return total_ones + best