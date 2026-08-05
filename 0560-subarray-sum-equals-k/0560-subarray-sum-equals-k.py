class Solution(object):
    def subarraySum(self, nums, k):

        sumCountMap = {0: 1}

        result = 0
        prefixSum = 0

        for num in nums:
            prefixSum += num

            if prefixSum - k in sumCountMap:
                result += sumCountMap[prefixSum - k]

            sumCountMap[prefixSum] = sumCountMap.get(prefixSum, 0) + 1

        return result
        