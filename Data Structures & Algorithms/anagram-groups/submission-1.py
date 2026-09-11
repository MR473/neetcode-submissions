class Solution:
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        h = {}
        for i in range(len(strs)):
            k = [0] * 26
            for c in strs[i]:
                k[ord(c)-ord('a')] += 1
            temp = h.get(str(k), [])
            temp.append(strs[i])
            h[str(k)] = temp
        return list(h.values())

