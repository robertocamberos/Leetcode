class Solution:
    def climbStairs(self, n: int) -> int:
        
        second = 1
        first = 1
        
        for i in range(n-1):
            tmp = first
            first = first + second
            second = tmp
            
            
        return first