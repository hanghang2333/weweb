class Solution(object):
    def charint(self,s):
        return ord(s)-ord('A')+1
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        zs = [1]
        start = 1
        for i in range(1,len(s)):
            start = start*26
            zs.append(start)
        zs.reverse()
        print(zs)
        res = 0
        for i in range(len(s)):
            res = res + zs[i]*self.charint(s[i])
        return res
a = Solution()
print a.titleToNumber("")
