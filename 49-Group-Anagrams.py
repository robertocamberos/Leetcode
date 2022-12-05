class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)
        for word in strs:
            tmp = [0] * 26
            for c in word:
                tmp[ord(c) - ord('a')] += 1
            mappings[tuple(tmp)].append(word)
        return mappings.values()