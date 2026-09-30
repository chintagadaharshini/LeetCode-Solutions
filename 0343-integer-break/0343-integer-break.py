class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1

        for j in range(3, n + 1):
            for i in range(1, j):
                # Either keep (j - i) whole or use its optimal break
                dp[j] = max(dp[j], i * max(j - i, dp[j - i]))
        return dp[n]