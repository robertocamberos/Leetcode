class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i <= 1:
                return 0
                
            if i not in memo:
                memo[i] = min(cost[i-1] + dfs(i-1), cost[i-2] + dfs(i-2))
                
            return memo[i]
            
        memo = {}
        return dfs(len(cost))