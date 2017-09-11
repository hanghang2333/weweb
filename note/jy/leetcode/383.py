class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict2 = {}
        for i in magazine:
            if i in dict2:
                dict2[i] = dict2[i]+1
            else:
                dict2[i] = 1
        for i in ransomNote:
            if i not in dict2 or dict2[i]==0:
                return False
            else:
                dict2[i] = dict2[i]-1
        return True
