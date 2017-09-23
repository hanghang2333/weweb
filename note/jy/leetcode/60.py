class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nn = [1]
        for i in range(1,n):
            nn.append(nn[-1]*i)
            #nn[i] =nn[i-1]*i
        nn = nn[1:]
        nn.reverse()
        res = []
        resbak = [i+1 for i in range(n)]#1,2,3,4
        idx = 0
        k = k -1
        while k!=0:
            nowidx = k/nn[idx]
            k = k % nn[idx]
            res.append(resbak[nowidx])
            resbak.remove(resbak[nowidx])
            idx = idx + 1
        res = res + resbak
        res = [str(i) for i in res]
        return ''.join(res)
a = Solution()
print(a.getPermutation(100,1234))
