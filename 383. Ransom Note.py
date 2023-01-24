class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        letters = collections.Counter(magazine)
        
        for char in ransomNote:
            if char in letters:
                if letters[char] != 0:
                    letters[char] -= 1
                else:
                    return False
            else:
                return False
        return True