class Solution(object):
    def back(self,res,tmpres,nums,tag,nowlen,alllen):
        import copy
        if nowlen==alllen:
            res.add(tuple(tmpres))
            return
        else:
            i = 0
            while i<alllen:
                if i>0 and nums[i-1]==nums[i] and tag[i-1]==False:
                    i = i + 1
                    continue
                if tag[i]==0:
                    tmpresbak = copy.deepcopy(tmpres)
                    tmpresbak.append(nums[i])
                    tag[i]=1
                    self.back(res,tmpresbak,nums,tag,nowlen+1,alllen)
                    tag[i]=0
                #while i<alllen-1 and nums[i+1]==nums[i]:
                #    i = i + 1
                i = i + 1

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        tmpres = []
        tag = [0 for i in range(len(nums))]
        self.back(res,tmpres,nums,tag,0,len(nums))
        #print(res)
        res = [list(i) for i in res]
        return len(res)

a = Solution()
print(a.permuteUnique([-1,2,-1,2,1,-1,2,1]))
