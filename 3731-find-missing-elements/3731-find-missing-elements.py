class Solution(object):
    def findMissingElements(self, nums):
        num_set=set(nums)
        ans=[]
        maximum=max(nums)
        minimum=min(nums)
        for i in range(minimum,maximum+1):
            if i not in num_set:
                ans.append(i)
        return ans

        