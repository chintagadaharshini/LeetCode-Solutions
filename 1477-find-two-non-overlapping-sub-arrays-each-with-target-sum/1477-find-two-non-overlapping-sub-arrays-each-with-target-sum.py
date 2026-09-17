class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        
        INF = float('inf')
        best = [INF] * n
        
        left = 0
        curr = 0
        ans = INF
        min_len = INF

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                # A previous subarray must end before 'left'
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                min_len = min(min_len, length)

            # Best subarray found so far up to this index
            best[right] = min_len

        return -1 if ans == INF else ans