class Solution(object):
    def solve(self,n):
        res = set()
        for i in range(1,int(n**0.5+1)):
            if i not in res:
                if n%i==0:
                    res.add(i)
                    res.add(n/i)
            else:
                break
        print(res)
        return res
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return True
        return sum(self.solve(num))==num*2
a = Solution()
print(a.checkPerfectNumber(28))
