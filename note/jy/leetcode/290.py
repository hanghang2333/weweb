class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = s
        paset = {}
        pa = ''
        idx = 0
        for i in pattern:
            if i in paset:
                pa = pa+str(paset[i])
            else:
                paset[i] = idx
                pa = pa +str(paset[i])
                idx = idx + 1
        stset = {}
        st = ''
        idx = 0
        strr = s.split()
        for i in strr:
            if i in stset:
                st = st+str(stset[i])
            else:
                stset[i] = idx
                st = st +str(stset[i])
                idx = idx + 1
        return st==pa
a = Solution()
print(a.wordPattern("abba", "dog cat cat dog"))
