class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        res = [[1]]
        for i in range(1,numRows):
            tmp = [0]+res[i-1]+[0]
            tmp1 = [tmp[j]+tmp[j+1] for j in range(i+1)]
            res.append(tmp1)
        return res
a = Solution()
print(a.generate(5))
