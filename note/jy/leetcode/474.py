class Solution(object):
    def findMaxForm(self, strs, m, n):
        '''
        maxnum = 0
        nownum = 0
        nowinx = 0
        strlist = sorted(strs,key=len)
        he = len(strlist)
        res = 0
        for i in range(he):
            if len(strlist[i])>m+n:
                return res
            tmp0 = 0
            tmp1 = 0
            for j in strlist[i]:
                if j == '0':
                    tmp0 = tmp0 + 1
                else:
                    tmp1 = tmp1 + 1
            #print(tmp0,tmp1,m,n)
            if tmp0<=m and tmp1<=n:
                m = m - tmp0
                n = n - tmp1
                res = res + 1
        strs = sorted(strs,key=len)
        #print(strs)
        maxnum = [0]
        nownum = 0
        nowinx = 0
        self.f(strs,nowinx,maxnum,nownum,m,n)
        return maxnum[0]
        '''
        dp = [[0]*(n+1) for _ in range(m+1)]
        def count(s):
            return sum(1 for c in s if c=='0'),sum(1 for c in s if c=='1')
        for s0,s1 in [count(s) for s in strs]:
            for x in range(m,-1,-1):
                for y in range(n,-1,-1):
                    if x>=s0 and y>=s1:
                        dp[x][y] = max(1+dp[x-s0][y-s1],dp[x][y])
        return dp[m][n]
    def f(self,strs,nowinx,maxnum,nownum,m,n):
        if nowinx==len(strs) or m==0 or n==0:
            return
        he = len(strs)
        for i in range(nowinx,he):
            if len(strs[i])>m+n:
                continue
            #print(i,'i',m,n)
            tmp0 = 0
            tmp1 = 0
            for j in strs[i]:
                if j == '0':
                    tmp0 = tmp0 + 1
                else:
                    tmp1 = tmp1 + 1
            if tmp0<=m and tmp1<=n:
                #print(nownum,m,n)
                maxnum[0] = max(maxnum[0],nownum+1)
                self.f(strs,i+1,maxnum,nownum+1,m-tmp0,n-tmp1)

a = Solution()
'''
["111","1000","1000","1000"]
9
3
'''
print a.findMaxForm(["10","0001","111001","1","0","10","0001","111001","1","0","10","0001","111001","1","0","10","0001","111001","1","0","10","0001","111001","1","0","10","0001","111001","1","0"],13,14)
print a.findMaxForm(["111","1000","1000","1000"],9,3)
