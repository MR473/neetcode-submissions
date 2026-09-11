class Solution:
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        h = defaultdict(list)
        for i in range(len(strs)):
            k = [0] * 26
            for c in strs[i]:
                k[ord(c)-ord('a')] += 1
            h[tuple(k)].append(strs[i])
        return list(h.values())