class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        res = 0
        for i in range(len(s)):
            res += countPalindrome(s, i, i)
            res += countPalindrome(s, i, i + 1)
        return res