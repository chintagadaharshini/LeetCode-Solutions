class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n == 1:
            return 1
        if n == 2:
            return 2

        x = 1
        while x <= n:
            x <<= 1

        return x













