class Solution(object):
    def hs(self,nums,target,now,resnow,res,inx):
        if target == now:
            h = False
            tmp1 = sorted(resnow)
            for i in res:
                #print(resnow,res)
                tmp2 = sorted(i)
                if tmp1==tmp2:
                    h = True
                #    print(resnow)
            if h == False:
                res.append(resnow)
            return
        for i in range(inx,len(nums)):
            if now+nums[i]<=target:
                tmp = []
                for j in resnow:
                    tmp.append(j)
                tmp.append(nums[i])
                self.hs(nums,target,now+nums[i],tmp,res,i+1)
                tmp = tmp[0:-1]
                #self.hs(nums,target,now,tmp,res,i+1)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
        [
         [1, 7],
         [1, 2, 5],
         [2, 6],
         [1, 1, 6]
        ]
        """
        n = len (candidates)
        res = []
        resnow = []
        self.hs(candidates,target,0,resnow,res,0)
        return res
a = Solution()
print a.combinationSum2([2,3,6,7],7)
