class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Map = {}
        stack = []
        for num in nums2:
            while len(stack) != 0 and stack[-1] < num:
                Map[stack.pop()] = num
            stack.append(num)
        for i in range(len(nums1)):
            nums1[i] = Map.get(nums1[i],-1)
        return nums1
        