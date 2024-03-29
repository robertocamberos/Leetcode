class Solution:
    def countLessEqual(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(matrix[row][col], larger)
                row -= 1
            else:
                smaller = max(matrix[row][col], smaller)
                count += row + 1
                col += 1
        return count, smaller, larger
        
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start, end = matrix[0][0], matrix[n-1][n-1]
        while start < end:
            mid = start + (end-start) / 2
            smaller, larger = matrix[0][0], matrix[n-1][n-1]
            
            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)
            if count == k:
                return smaller
            if count < k:
                start = larger
            else:
                end = smaller
        return start