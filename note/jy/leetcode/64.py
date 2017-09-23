class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        maxn = float('inf')
        dp = [[0]*n+1 for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = maxn
        for i in range(m+1):
            dp[i][0] = maxn
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    dp[i][j] = grid[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[m][n]
