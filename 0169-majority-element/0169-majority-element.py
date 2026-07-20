class Solution(object):
    def majorityElement(self, nums):
        counts = {}
        for num in nums:
            if num in counts:
                counts[num]+=1
            else:
                counts[num]=1
            if counts[num]>len(nums)//2:
                return num
        