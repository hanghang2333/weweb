class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if k<=1:
            return nums
        if k==n:
            return [max(nums)]
        maxidx = -3
        maxn = float('-inf')
        res = []
        for i in range(n-k+1):
            start = i
            end = i+k-1
            #print('w',i,start,end,maxidx)
            if i>n:
                pass
            else:
                if maxidx+(k-1)>=end:
                     if nums[end]>=maxn:
                         maxn = nums[end]
                         maxidx = end
                else:
                    maxn = max(nums[start:end+1])
                    for j in range(start,end+1,1):
                        if maxn == nums[j]:
                            maxidx = j
                            break
            #print('now',maxidx,maxn)
            res.append(maxn)
        return res

a = Solution()
print(a.maxSlidingWindow([7,2,4],2))
