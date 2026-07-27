class Solution(object):
    def maxProduct(self, nums):
        maximum=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                pro=(nums[i]-1)*(nums[j]-1)
                maximum=max(maximum,pro)
        return maximum
