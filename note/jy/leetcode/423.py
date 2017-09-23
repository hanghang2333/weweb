class Solution(object):
    def solution(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        longgest = 0
        n = len(A)
        dp = [1 for _ in range(n)]
        ori = A[1]-A[0]
        for i in range(1,n):
            if A[i]-A[i-1]==ori:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 2
                ori = A[i]-A[i-1]
        dp.append(1)
        res = []
        for i in range(n):
            if dp[i]>dp[i+1] and dp[i]>=3:
                res.append(dp[i])
        r = 0
        for i in res:
            if i>3:
                r = r+(i-1)*(i-2)/2
            else:
                r = r+1
        return r
    def numberOfArithmeticSlices(self, A):
        res = 0
        chamax = (len(A)-3)/2
        print(chamax)
        for cha in range(chamax+1):
            for i in range(0,cha+1):
                tmp = A[i::cha+1]
                res = res + self.solution(tmp)
        return res
a = Solution()
print(a.numberOfArithmeticSlices([7,7,7,7]))
