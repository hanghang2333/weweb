class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = sorted(nums,reverse=True)
        dict1 = {i:inx for inx,i in enumerate(res)}
        for inx,i in enumerate(nums):
            if dict1[i]>=3:
                nums[inx] = str(dict1[i]+1)
            elif dict1[i]==0:
                nums[inx]="Gold Medal"
            elif dict1[i]==1:
                nums[inx] ="Silver Medal"
            else:
                nums[inx] =  "Bronze Medal"
        return nums
a = Solution()
print a.findRelativeRanks([5,4,3,2,1])
