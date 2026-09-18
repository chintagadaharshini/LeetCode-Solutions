class Solution(object):
    def maxNumOfSubstrings(self, s):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        candidates = []

      
        for i in range(n):

            idx = ord(s[i]) - ord('a')

            if first[idx] != i:
                continue

            l = i
            r = last[idx]

            j = l
            valid = True

            while j <= r:
                curr = ord(s[j]) - ord('a')

             
                if first[curr] < l:
                    valid = False
                    break

                r = max(r, last[curr])

                j += 1

            if valid:
                candidates.append((l, r))

        candidates.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in candidates:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result    