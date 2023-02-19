class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(i,T):
            if (i == 0):
                if T % coins[i] == 0:
                    return T // coins[i]
                else:
                    return float("inf")
                
            notTake = dfs(i-1,T)
            
            take = float("inf")
            
            if coins[i] <= T:
                take = 1 + dfs(i,T - coins[i])
            
            return min(notTake, take)
        res = dfs(len(coins)-1,amount)
        if res != float('inf'):
            return res
        return -1