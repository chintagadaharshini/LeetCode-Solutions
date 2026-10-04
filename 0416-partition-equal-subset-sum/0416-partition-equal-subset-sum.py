class Solution(object):
    def canPartition(self, nums):
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False
        target=total_sum//2
        memo={}
        def can_find(index,remaining):
            if remaining==0:
                return True
            if remaining<0 or index>=len(nums):
                return False
            if (index,remaining) in memo:
                return memo[(index,remaining)]
            result=can_find(index+1,remaining-nums[index]) or can_find(index+1,remaining)
            memo[(index,remaining)]=result
            return result
        return can_find(0,target)
        