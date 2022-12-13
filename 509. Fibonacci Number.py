class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev2 = 0
        prev = 1
        
        for i in range(2,n+1):
            print(i)
            cur = prev + prev2
            prev2 = prev
            prev = cur
        return prev