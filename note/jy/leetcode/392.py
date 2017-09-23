class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        start = 0
        for i in t:
            if i ==s[start]:
                start = start + 1
        return start==len(s)
