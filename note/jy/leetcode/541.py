class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        res = []
        duan = len(s)/(2*k)
        if duan*(2*k)<len(s):
            duan = duan + 1
        for i in range(duan):
            start = i*2*k
            end = start+2*k
            mid = start+k
            tmp = s[start:mid]
            tmp.reverse()
            res.extend(tmp)
            res.extend(s[mid:end])
        res.extend(s[duan*(2*k):])
        return ''.join(res)
a = Solution()
print(a.reverseStr('abcdedf',2))
