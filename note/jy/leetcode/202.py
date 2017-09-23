class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        s.add(n)
        while n!=1:
            allnum =sum([int(i)*int(i) for i in list(str(n))])
            if allnum in s:
                return False
            else:
                n = allnum
            s.add(n)
        return True

a = Solution()
print(a.isHappy(23))
