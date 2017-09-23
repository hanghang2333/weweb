class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for inx,i in enumerate(nums):
            if i in d:
                tmp = d[i]
                tmp.append(inx)
                d[i] = tmp
            else:
                d[i] = [inx]
        #print(d)
        for i in range(len(nums)):
            if target-nums[i] in d:
                if len(d[target-nums[i]])==2:
                    return d[target-nums[i]]
                else:
                    if d[target-nums[i]][0]!=i:
                        return [i,d[target-nums[i]][0]]
a = Solution()
print(a.twoSum([2,2,4],4))
