class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
        change = 0
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                pass
            else:
                if i==1:
                    nums[i-1]=nums[i]
                    change = change + 1
                elif nums[i]>=nums[i-2]:
                    nums[i-1] = nums[i]
                    change = change + 1
                else:
                    nums[i]=nums[i-1]
                    change = change + 1
        return change<=1

a = Solution()
print(a.checkPossibility([3,4,2]))
