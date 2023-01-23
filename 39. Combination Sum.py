class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, cur):
            if total < 0 or i == len(candidates):
                return
            if total == 0:
                res.append(cur[:])
                return
            
            
            cur.append(candidates[i])
            dfs(i,total - candidates[i], cur)
            cur.pop()
            
            dfs(i+1, total,cur)
            
            
        dfs(0,target,[])
        return res