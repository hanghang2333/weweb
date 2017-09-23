class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        lenmin = min([len(i) for i in strs])
        idx = 0
        for i in range(lenmin):
            tmpset = set([j[i] for j in strs])
            if len(tmpset)==1:
                idx = idx + 1
            else:
                break
        res = strs[0][0:idx]
        return res
a = Solution()
print(a.longestCommonPrefix(['adcswrf']))
