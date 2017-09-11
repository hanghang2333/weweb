class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["ate", "eat","tea"],
        ["nat","tan"],
        ["bat"]
        """
        res = []
        d = {}
        for i in range(len(strs)):
            tmp = tuple(sorted(strs[i]))
            if tmp in d:
                d[tmp] = d[tmp]+[i]
            else:
                d[tmp] = [i]
        for key in d:
            tmp = []
            for value in d[key]:
                tmp.append(strs[value])
            res.append(tmp)
        return res
a = Solution()
print a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
