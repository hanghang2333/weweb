class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n==1:
            return 10
        if n==0:
            return 0
        for i in range(n,1,-1):
            tmp = 1
            start = 10
            j = i#2
            while j>0:
                tmp = tmp*start
                start = start-1
                j = j -1
            tmp = tmp/10*9
            res = res + tmp
        return res+10
