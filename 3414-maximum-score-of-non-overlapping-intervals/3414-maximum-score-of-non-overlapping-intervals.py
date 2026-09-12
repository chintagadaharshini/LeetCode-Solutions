class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []

        for i, (l, r, w) in enumerate(intervals):
            arr.append((r, l, w, i))

        # Sort by ending position
        arr.sort()

        ends = [x[0] for x in arr]

        import bisect

        # prev[i] = number of intervals before i
        # whose ending point is < current starting point
        prev = [0] * n

        for i in range(n):
            l = arr[i][1]
            prev[i] = bisect.bisect_left(ends, l)

        # dp[k][i] = (maximum score, lexicographically smallest indices)
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):

            for i in range(1, n + 1):

                # Don't take current interval
                skip = dp[k][i - 1]

                r, l, w, idx = arr[i - 1]

                # Take current interval
                p = prev[i - 1]

                old_score, old_indices = dp[k - 1][p]

                new_indices = tuple(sorted(old_indices + (idx,)))

                take = (
                    old_score + w,
                    new_indices
                )

                # Choose better score
                if take[0] > skip[0]:
                    dp[k][i] = take

                elif take[0] < skip[0]:
                    dp[k][i] = skip

                else:
                    # Same score -> lexicographically smaller indices
                    dp[k][i] = min(take, skip)

        return list(dp[4][n][1])