class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        end = 0
        if n%2==0:
            end = n/2
        else:
            end = n/2+1
        dp = [0 for i in range(2*end+1)]#0--n
        dp[2]=1
        for j in range(2,end+1):
            now = j*2
            dp[now] = 1+dp[now/2]
            dp[now-1] = min(1+dp[now-2],1+dp[now])
        #print(dp)
        return dp[n]
    def integerReplacement(self, n):
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn

a = Solution()
print(a.integerReplacement(10000000))
