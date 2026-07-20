class Solution(object):
    def majorityElement(self, nums):
        counts={}
        treshold=len(nums)//2
        for num in nums:
            counts[num]=counts.get(num,0)+1
            if counts[num]>treshold:
                return num

        