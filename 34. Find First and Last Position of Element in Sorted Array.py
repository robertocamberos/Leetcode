class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [-1,-1]
        if len(nums) == 0:
            return res
        while l < r:
            m = (l + r) // 2
            
            if nums[m] < target:
                l = m+1
            else:
                r = m
        if nums[l] != target:
            return res
        else:
            res[0] = l
        r = len(nums)-1
        while l < r:
            m = (l + r) // 2 + 1
            
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        res[1] = r
        return res
        