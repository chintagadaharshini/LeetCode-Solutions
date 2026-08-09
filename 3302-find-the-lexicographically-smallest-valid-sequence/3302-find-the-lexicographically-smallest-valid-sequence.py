class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # last[j] = latest index in word1 that can match
        # word2[j] while matching word2[j:] exactly.
        last = [-1] * m

        i = n - 1
        j = m - 1

        # Build suffix feasibility
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        used_mismatch = False

        # Greedily choose the smallest possible indices
        for i in range(n):

            if j == m:
                break

            # Case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: use our one allowed mismatch
            elif not used_mismatch:
                # If this is the last character, no suffix remains.
                #
                # Otherwise, we need enough room to match
                # word2[j+1:] exactly.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    used_mismatch = True
                    j += 1

        if j == m:
            return ans

        return []
        