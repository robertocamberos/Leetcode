class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0])
        top, bot = 0, len(matrix)
        
        while l < r and top < bot:
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bot):
                res.append(matrix[i][r-1])
            r -= 1
            
            if not (top < bot and l < r):
                break
            
            
            for i in range(r-1,l-1,-1):
                res.append(matrix[bot-1][i])
            bot -= 1
            
            
            for i in range(bot-1,top-1,-1):
                res.append(matrix[i][l])
            l += 1
        return res