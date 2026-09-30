class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num

        memo = [-1] * (max_val + 1)

        def solve(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return points[0]
            if i == 1:
                return max(points[0], points[1])
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(solve(i - 1), points[i] + solve(i - 2))
            return memo[i]

        return solve(max_val)