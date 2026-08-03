class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        mp = {}
        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                mp[nums2[i]] = -1
            else:
                mp[nums2[i]] = stack[-1]

            stack.append(nums2[i])

        ans = []

        for num in nums1:
            ans.append(mp[num])

        return ans