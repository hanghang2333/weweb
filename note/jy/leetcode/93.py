class Solution:
    def slove(self,s):
        def isvaild(s):
            if len(s)>3 or len(s)==0 or s[0]=='0' and len(s)>1 or int(s)>255:
                return False
            return True
        res = []
        n = len(s)
        for i in range(1,min(4,n-2)):
            for j in range(i+1,min(i+4,n-1)):
                for k in range(j+1,min(j+4,n)):
                    s1,s2,s3,s4 = s[0:i],s[i:j],s[j:k],s[k:]
                    if isvaild(s1) and isvaild(s2) and isvaild(s3) and isvaild(s4):
                        res.append('.'.join([s1,s2,s3,s4]))
        return res
a = Solution()
print(a.slove('25525511135'))
