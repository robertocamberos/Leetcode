class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counts = {}
        for word in words:
            counts[word] = 1 +  counts.get(word,0)
        indexes = []
        n = len(s)
        num = len(words)
        Len = len(words[0])
        for i in range(n - num * Len + 1):
            seen = {}
            j = 0
            while j < num:
                word = s[(i + j * Len): (i + (j + 1) * Len)]
                if word in counts:
                    seen[word] = 1 + seen.get(word,0)
                    if seen[word] > counts.get(word,0):
                        break
                else:
                    break
                j += 1
            if j == num:
                indexes.append(i)
        return indexes
        