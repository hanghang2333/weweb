class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        fs = False
        if num<0:
            fs = True
            num = -1*num
        res = []
        while num != 0:
            now = num/7
            ys = num%7
            res.append(ys)
            num = now
        print(res)
        res.reverse()
        res = [str(i) for i in res]
        r = ''.join(res)
        if fs==True:
            r = '-'+r
        return r

a = Solution()
print(a.convertToBase7(-7))
