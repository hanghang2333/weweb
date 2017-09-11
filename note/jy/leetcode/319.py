class Solution(object):
    def ys(self,n):
        count = 0
        for i in range(1,n+1):
            if n%i==0:
                count = count + 1
        return count
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        inx = 1
        while inx*inx<=n:
            count = count + 1
            inx = inx + 1
        return count
a = Solution()
print a.bulbSwitch(172)
