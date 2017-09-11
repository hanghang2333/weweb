class Solution(object):
    def inter(self,n,d):
        if n == 1:
            return 1
        maxvalue = 1
        tag = 0
        for i in range(1,n):
            tmp2 = 0
            if n-i in d:
                tmp2 = i*d[n-i]
            else:
                tmp2 = i*self.inter(n-i,d)
            if tmp2>maxvalue:
                tag = i
                maxvalue = tmp2
            if i*(n-i)>maxvalue:
                maxvalue = i*(n-i)
        d[n] = maxvalue
        return maxvalue
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        res = self.inter(n,d)
        return res
a = Solution()
print a.integerBreak(5)
