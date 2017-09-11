# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def bs(self,nums,key):
        left = 0
        right = len(nums)
        while left+1<right:
            medium = (left+right)/2
            #print('m',left,right,medium)
            if nums[medium]<key:
                left = medium
            elif nums[medium]>key:
                right = medium
            else:
                return medium
        if right>=len(nums):
            right = -1
        return right
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        rrr = []
        start = [i[0] for i in intervals]
        sortstart = sorted(start)
        sdict = {i:inx for inx,i in enumerate(start)}
        for i in intervals:
            end = i[1]
            inx = self.bs(sortstart,end)
            if inx == -1:
                rrr.append(-1)
            else:
                rn = sortstart[inx]
                ri = sdict[rn]
                rrr.append(ri)
        return rrr

a = Solution()
print a.bs([0,1,2,3],3)
print a.findRightInterval([[1,2],[2,3],[0,1],[3,4]])
