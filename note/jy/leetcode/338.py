class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for _ in range(num+1)]
        for i in range(1,num+1):
            #print(i,'w',dp[i>>1],i&1,dp[i>>1]+i&1)
            dp[i] = dp[i>>1]+(i&1)
            #print(i,dp[i>>1],dp[i])
        return dp

class Solution1(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        res = math.log(num,4)
        return int(res)==res
