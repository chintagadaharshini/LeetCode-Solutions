class Solution(object):
    def climbStairs(self, n):
        memo={}
        def helper(k):
            if k==1:
                return 1
            if k==2:
                return 2
            if k in memo:
                return memo[k]
            memo[k]=helper(k-1)+helper(k-2)
            return memo[k]
        return helper(n)

        