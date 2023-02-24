class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charFreq = {}
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            charFreq[s[r]] = 1 + charFreq.get(s[r],0)
            maxFreq = max(maxFreq, charFreq[s[r]])
            
            if (r-l+1) - maxFreq > k:
                charFreq[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
            
        return res        