class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        double = 0
        remove = 0
        for i in nums:
            if i in d:
                double = i
            else:
                d[i] = 1
        for i in range(1,len(nums)+1):
            if i not in d:
                remove = i
                break
        return [double,remove]
