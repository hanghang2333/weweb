class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        def calculate(i, j):
            print(i,j)
            if dp[i][j] or j == i + 1: # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in xrange(i+1, j): # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)

a = Solution()
a.maxCoins([3,1,5,8])
