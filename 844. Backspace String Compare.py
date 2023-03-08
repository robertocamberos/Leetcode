class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                if S[i] == '#':
                    backS += 1
                else:
                    backS -= 1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                if T[j] == '#':
                    backT += 1
                else:
                    backT -= 1
                j -= 1
            if (i < 0 or j < 0 or S[i] != T[j]):
                return i == j == -1
            i, j = i - 1, j - 1
            