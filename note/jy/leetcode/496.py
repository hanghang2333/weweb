class Solution(object):
    def nextGreaterElements(self, findNums,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for idx,i in enumerate(nums):
            d[i] = idx
        fs = set(findNums)
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        r = []
        for i in findNums:
            r.append(res[d[i]])
        return r
