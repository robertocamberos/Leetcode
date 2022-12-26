class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1)-1
        j = len(num2)-1
        res = ""
        carry = 0
        while i >= 0 or j >= 0 or carry == 1:
            if i < 0:
                x = 0
            else:
                x = num1[i]
                
            if j < 0:
                y = 0
            else:
                y = num2[j]
            tmp = int(x) + int(y) + carry  
            res += str(tmp % 10)
            carry = tmp // 10
            i -= 1
            j -= 1
            
        return res[::-1]
            
            