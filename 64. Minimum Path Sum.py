class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 for j in range(cols)] for i in range(rows)]
        def dfs(i,j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = grid[i][j] + dfs(i-1,j)
            left = grid[i][j] + dfs(i,j-1)
            dp[i][j] = min(up, left)
            return dp[i][j]
        return dfs(len(grid)-1,len(grid[0])-1)