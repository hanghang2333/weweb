class Solution(object):
    def findk(self,k):
        tmp = int((k*2)**0.5-1)
        while tmp*(tmp+1)/2<k:
            tmp = tmp + 1
        pre = tmp*(tmp-1)/2
        now = k-pre
        return tmp,now
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        pass

a = Solution()
print(a.findk(4))
