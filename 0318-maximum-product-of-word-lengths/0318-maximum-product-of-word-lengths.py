class Solution(object):
    def maxProduct(self, words):

        n = len(words)

        # Create sets only once
        word_sets = []
        for word in words:
            word_sets.append(set(word))

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if word_sets[i].isdisjoint(word_sets[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans