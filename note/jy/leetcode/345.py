class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yy = ''
        inx = []
        s=list(s)
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                inx.append(i)
                yy = yy+s[i]
        yy = yy[::-1]

        for i in range(len(inx)):
            s[inx[i]] = yy[i]
        return ''.join(s)
