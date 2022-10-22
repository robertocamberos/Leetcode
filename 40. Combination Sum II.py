class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, target, cur):
            if target == 0:
                res.append(cur[:])
                return
            if i == len(candidates) or target < 0:
                return
            
            cur.append(candidates[i])
            dfs(i+1, target - candidates[i],cur)
            cur.pop()
            
            while i+1< len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, target, cur)
            
        dfs(0,target, [])
        return res