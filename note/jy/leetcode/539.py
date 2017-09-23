class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def cmp(str1,str2):
            str1 = int(str1.replace(':',''))
        timelist = sorted(timePoints,key=lambda x:int(x.replace(':','')))
        #print(timelist)
        def timej(str1,str2):
            h1,m1 = int(str1[0:2]),int(str1[3:])
            h2,m2 = int(str2[0:2]),int(str2[3:])
            res = (h2-h1)*60 + (m2-m1)
            return res
        #print(timej("02:01","03:00"))
        minn = timej(timelist[0],timelist[1])
        for i in range(1,len(timelist)):
            minn = min(minn,timej(timelist[i-1],timelist[i]))
            #print(minn)
        minn = min(minn,24*60-timej(timelist[0],timelist[-1]))
        return minn

a = Solution()
print(a.findMinDifference(["01:01","02:01","03:00"]))

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)==len(word2) and len(word1)==1:
            return 2 if word1!=word2 else 0
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(n+1):
            dp[0][i] = i
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+2,dp[i-1][j]+1,dp[i][j-1]+1)
        #print(dp)
        return dp[m][n]
