class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 != 0:
            return False

        # dp[i][j] stores the possible open bracket counts
        # when reaching cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                # Get possible counts from the top and left cells
                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]

                if j > 0:
                    prev |= dp[i][j - 1]

                for balance in prev:
                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # A closing bracket cannot appear without
                    # a matching opening bracket
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        # The path is valid if it ends with balance 0
        return 0 in dp[m - 1][n - 1]