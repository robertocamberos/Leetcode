class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        freq = [False] * len(nums)
        def dfs(i,cur,freq):
            if len(cur) == len(nums):
                res.append(cur[::])
                return
            
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i] = True
                    cur.append(nums[i])
                    dfs(i,cur,freq)
                    cur.pop()
                    freq[i] = False
        dfs(0,[],freq)
        return res