class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        for i in xrange(2,n):
            tmp = n
            flag = False
            while tmp!=0:
                if tmp%i==1:
                    tmp = tmp/i
                else:
                    flag = True
                    break
            if flag == False:
                return i

a = Solution()
print(a.smallestGoodBase(1000000000000000000))
