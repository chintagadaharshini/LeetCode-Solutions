class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(arr)

        rank = {}
        curr_rank = 1

        for num in sorted_arr:
            if num not in rank:
                rank[num] = curr_rank
                curr_rank += 1

        ans = []

        for num in arr:
            ans.append(rank[num])

        return ans