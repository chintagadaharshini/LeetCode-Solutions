class Solution(object):
    def pivotIndex(self, nums):
        total=sum(nums)
        left_sum=0
        for i in range(0,len(nums)):
            right_sum=total-nums[i]-left_sum  
            if right_sum==left_sum:
                return i
            left_sum+=nums[i]
        return -1
        