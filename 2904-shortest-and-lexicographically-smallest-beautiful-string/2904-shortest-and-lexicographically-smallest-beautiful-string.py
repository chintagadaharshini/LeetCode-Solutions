class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)

        left = 0
        ones = 0
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Window has exactly k ones
            while ones == k:
                # Remove leading zeros to make the substring as short
                # and lexicographically smallest as possible
                while left <= right and s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                # Update answer
                if ans == "" or len(curr) < len(ans) or \
                   (len(curr) == len(ans) and curr < ans):
                    ans = curr

                # Move left past the first 1
                if s[left] == '1':
                    ones -= 1
                left += 1

        return ans