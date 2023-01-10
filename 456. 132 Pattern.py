class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curMin = nums[0]
        
        for n in nums:
            while stack and n >= stack[-1][0]:
                stack.pop()
                
            if stack and n > stack[-1][1]:
                return True
            
            curMin = min(curMin, n)
            stack.append([n, curMin])
        return False