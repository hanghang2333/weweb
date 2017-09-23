class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        lll = n
        n = len(flowerbed)
        def isvalid(idx):
            if idx>=0 and idx<n:
                return True
            return False
        a = [0 for i in range(len(flowerbed))]
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                left,now,right = i-1,i,i+1
                if isvalid(left):
                    a[left] = 1
                if isvalid(now):
                    a[now] = 1
                if isvalid(right):
                    a[right] = 1
        if sum(a)==n:
            return 0>=lll
        res = 0
        start = 0
        while a[start]!=0:
            start = start + 1
        print(a,start)
        while start<len(flowerbed):
            end = start+1
            if end>=len(flowerbed):
                res = res + 1
                break
            while end<n and a[end]==0:
                end = end + 1
            print(start,end)
            jv = end - start
            res = res + (jv+1)/2
            while end<n and a[end]!=0:
                end = end + 1
            if end==n-1 and a[end]!=0:
                break
            start = end
        print(res)
        return res>=lll

a = Solution()
print(a.canPlaceFlowers([1,0,0,0,0,1],2))
