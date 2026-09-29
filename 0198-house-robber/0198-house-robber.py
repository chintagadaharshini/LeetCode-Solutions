class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [-1] * len(nums)

        def rob_from(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if memo[i] != -1:
                return memo[i]

            # Cache the result: max of skipping or robbing house i
            memo[i] = max(rob_from(i - 1), nums[i] + rob_from(i - 2))
            return memo[i]

        return rob_from(len(nums) - 1)