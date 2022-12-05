class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalSum = 0
        maxi = nums[0]
        
        for i,n in enumerate(nums):
            totalSum += n
            maxi = max(maxi, totalSum)
            if totalSum < 0:
                totalSum = 0
        return maxi