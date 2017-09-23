class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        orr = len(nums)
        orc = len(nums[0])
        if orr*orc!=r*c:
            return nums
        allnums = []
        for i in nums:
            for j in i:
                allnums.append(j)
        res = []
        inx = 0
        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(allnums[inx])
                inx = inx + 1
            res.append(tmp)
        return res
