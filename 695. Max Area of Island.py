class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def dfs(r,c,visit,curIsland):
            if (r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r,c))
            return 1 + dfs(r+1,c,visit,curIsland) + dfs(r-1,c,visit,curIsland) + dfs(r,c+1,visit,curIsland) + dfs(r,c-1,visit,curIsland)
            
            return curIsland
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    islands = max(islands, dfs(r,c,visit,0))
                    
        return islands