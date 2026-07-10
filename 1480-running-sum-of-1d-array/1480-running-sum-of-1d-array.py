class Solution(object):
    def runningSum(self, nums):
        total=0
        runningSum=[]
        for i in range(len(nums)):
            total+=nums[i]
            runningSum.append(total)
        return runningSum
