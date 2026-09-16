class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        r = 2 * k
        N = n + k - 1

        # Calculate C(N, r)
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (N - r + i) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD

        return ans