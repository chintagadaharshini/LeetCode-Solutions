class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        ans = 0

        for right in range(len(s)):

            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            length = right - left + 1

            if length > ans:
                ans = length

        return ans 