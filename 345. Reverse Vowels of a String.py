class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        while l <= r:
            if s[l].lower() in vowels and s[r].lower() in vowels:
                tmp = s[l]
                s = s[:l] + s[r] + s[l+1:]
                s = s[:r] + tmp + s[r+1:]
                l += 1
                r -= 1
            elif s[l].lower() in vowels and s[r].lower() not in vowels:
                r -= 1
            elif s[l].lower() not in vowels and s[r].lower() in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return s