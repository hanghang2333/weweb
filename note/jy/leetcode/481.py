class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        ori = [1,2,2]
        idx = 2
        while len(ori)<n:
            ori+=ori[idx]*[3-ori[-1]]
            idx += 1
        return ori[0:n].count(1)
