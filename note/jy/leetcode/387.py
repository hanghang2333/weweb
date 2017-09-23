class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for i in range(len(s)):
            if d[s[i]]<2:
                return i
        return -1
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
