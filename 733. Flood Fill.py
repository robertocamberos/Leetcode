class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visit = set()
        startColor = image[sr][sc]
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or
               image[r][c] != startColor or (r,c) in visit):
                return
            visit.add((r,c))
            image[r][c] = color
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        dfs(sr,sc)
        return image