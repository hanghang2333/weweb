class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        print(d)
        dk = min(d.values())
        if dk == 1:
            return False
        ys = []
        n = len(s)
        for i in range(dk,1,-1):
            if dk%i == 0 and n%i==0:
                ys.append(n/i)
        print(dk,ys)
        for i in ys:
            nowc = i
            flag = True
            for j in range(0,len(s)/nowc-1):
                if s[j*nowc:(j+1)*nowc] != s[(j+1)*nowc:(j+2)*nowc]:
                    flag = False
            if flag == True:
                return True
        return False
a = Solution()
print a.repeatedSubstringPattern("abddab")
