class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in range(len(ops)):
            if ops[i] == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif ops[i] == 'D':
                stack.append(2 * int(stack[-1]))
            elif ops[i] == 'C':
                stack.pop()
            else:
                stack.append(ops[i])
        res = 0
        for num in stack:
            res += int(num)
        return res
                