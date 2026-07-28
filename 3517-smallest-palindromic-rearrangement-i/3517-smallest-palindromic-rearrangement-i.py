from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        freq = Counter(s)

        left = []
        middle = ""

        for i in range(ord('a'), ord('z') + 1):
            ch = chr(i)

            if ch in freq:
                left.append(ch * (freq[ch] // 2))

                if freq[ch] % 2 == 1:
                    middle = ch

        left = "".join(left)
        right = left[::-1]

        return left + middle + right