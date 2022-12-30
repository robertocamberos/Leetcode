class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side_length = sum(matchsticks) // 4 
        square = [0] * 4 
        
        if sum(matchsticks) / 4 != side_length:
            return False
        matchsticks.sort(reverse = True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            used = set()
            for j in range(4):
                if square[j] + matchsticks[i] <= side_length and square[j] + matchsticks[i] not in used:
                    square[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    square[j] -= matchsticks[i]
                    used.add(square[j] + matchsticks[i])
            return False
            
        return backtrack(0)
        
        