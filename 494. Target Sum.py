class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = [0]
        def dfs(i, total):
            if i == len(nums) and total == target:
                res[0] += 1
                
            if i == len(nums):
                return
            
            dfs(i+1, total + nums[i])
            
            
            dfs(i+1, total - nums[i])
        dfs(0,0)
        return res[0]