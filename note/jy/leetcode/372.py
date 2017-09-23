class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        nowres = 1
        nowc = a
        for i in range(len(b)-1,-1,-1):
            nowres = (nowres*(nowc**b[i]%1337))%1337
            nowc = nowc**10%1337
        return nowres
a = Solution()
print(a.superPow(2,[1,3,1]))
