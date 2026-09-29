class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}

        def min_cost(i: int) -> int:
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            # Compute and cache the result
            memo[i] = cost[i] + min(min_cost(i + 1), min_cost(i + 2))
            return memo[i]

        return min(min_cost(0), min_cost(1))