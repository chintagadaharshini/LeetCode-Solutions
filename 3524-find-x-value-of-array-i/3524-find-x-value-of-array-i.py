class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k

        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Subarray containing only nums[i]
            new_dp[num % k] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * (num % k)) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            # Add all subarrays ending here to the answer
            for r in range(k):
                result[r] += dp[r]

        return result