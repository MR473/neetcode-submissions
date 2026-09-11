class Solution:
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        d = {}
        l = list()
        for i in range(len(strs)):
            x = sorted(strs[i])
            temp = d.get(str(x), [])
            temp.append(strs[i])
            d[str(x)] = temp
        return list(d.values())