#unsolution
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = sorted(list(set(s)))
        print(ss)
        inx = []
        for i in ss:
            for j in range(len(s)-1,-1,-1):
                if s[j]==i:
                    inx.append(j)
                    break
        print(inx)
        res = ''
        inxs = sorted(inx)
        for i in inxs:
            res = res+s[i]
        return res
a = Solution()
print(a.removeDuplicateLetters('cdacdcbc'))
