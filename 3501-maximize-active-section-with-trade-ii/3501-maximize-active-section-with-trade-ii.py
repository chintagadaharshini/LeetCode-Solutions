import bisect
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        # Build maximal runs of the string
        runs = []  # (char, start, end)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j

        # Extract 1-runs with flanking 0-run lengths (L = before, R = after)
        starts, ends, Lv, Rv = [], [], [], []
        for idx, (ch, st, en) in enumerate(runs):
            if ch == '1':
                L = (runs[idx - 1][2] - runs[idx - 1][1] + 1) if idx - 1 >= 0 else 0
                R = (runs[idx + 1][2] - runs[idx + 1][1] + 1) if idx + 1 < len(runs) else 0
                starts.append(st); ends.append(en)
                Lv.append(L); Rv.append(R)

        k = len(starts)
        NEG = float('-inf')

        # Sparse table over V = L+R (only ever queried for "middle" runs)
        if k > 0:
            V = [Lv[i] + Rv[i] for i in range(k)]
            sparse = [V]
            j = 1
            while (1 << j) <= k:
                prev = sparse[-1]
                half = 1 << (j - 1)
                length = k - (1 << j) + 1
                cur = [max(prev[x], prev[x + half]) for x in range(length)]
                sparse.append(cur)
                j += 1

            def range_max(l, r):
                if l > r:
                    return NEG
                length = r - l + 1
                kk = length.bit_length() - 1
                return max(sparse[kk][l], sparse[kk][r - (1 << kk) + 1])
        else:
            def range_max(l, r):
                return NEG

        ans = []
        for l, r in queries:
            if k == 0:
                ans.append(total_ones)
                continue

            lo = bisect.bisect_right(starts, l)      # first run with start > l
            hi = bisect.bisect_left(ends, r) - 1      # last run with end < r

            if lo > hi:
                ans.append(total_ones)
                continue

            if lo == hi:
                gain = min(Lv[lo], starts[lo] - l) + min(Rv[lo], r - ends[lo])
            else:
                g_first = min(Lv[lo], starts[lo] - l) + Rv[lo]
                g_last = Lv[hi] + min(Rv[hi], r - ends[hi])
                g_mid = range_max(lo + 1, hi - 1) if hi - 1 >= lo + 1 else NEG
                gain = max(g_first, g_last, g_mid)

            ans.append(total_ones + gain)

        return ans