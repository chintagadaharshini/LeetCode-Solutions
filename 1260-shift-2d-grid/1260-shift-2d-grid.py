class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        arr = sum(grid, [])
        k %= len(arr)
        arr = arr[-k:] + arr[:-k]
        return [arr[i:i+n] for i in range(0, len(arr), n)]