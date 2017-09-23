class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ss = set(s)
        for c in ss:
            if s.count(c)<k:
                return max(self.longestSubstring(i) for i in s.split(c))
        return len(s)
