class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        start = 0
        maxlength = 0
        for i in range(len(s)):
            if s[i] in used and used[s[i]]>=start:
                start = used[s[i]]+1
            else:
                maxlength = max(maxlength,i-start+1)
            used[s[i]] = i
        return maxlength
