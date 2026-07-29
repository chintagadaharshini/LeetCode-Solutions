from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        mid = ""
        cnt = [0] * 26
        total = 0

        for c in range(26):
            ch = chr(ord('a') + c)
            if freq[ch] % 2:
                mid = ch
            cnt[c] = freq[ch] // 2
            total += cnt[c]

        LIMIT = k

        def ways(counts):
            rem = sum(counts)
            ans = 1
            for x in counts:
                if x:
                    ans *= comb(rem, x)
                    if ans > LIMIT:
                        return LIMIT + 1
                    rem -= x
            return ans

        if ways(cnt) < k:
            return ""

        ans = []

        while total:
            for c in range(26):
                if cnt[c] == 0:
                    continue

                cnt[c] -= 1
                w = ways(cnt)

                if w >= k:
                    ans.append(chr(ord('a') + c))
                    total -= 1
                    break
                else:
                    k -= w
                    cnt[c] += 1

        left = "".join(ans)
        return left + mid + left[::-1]  