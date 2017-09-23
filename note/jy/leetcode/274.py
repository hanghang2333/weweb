class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        tot = 0
        arr = [0 for _ in range(n+1)]
        for i in citations:
            if i>=n:
                arr[n] = arr[n]+1
            else:
                arr[i] = arr[i]+1
        for i in range(n,-1,-1):
            tot = tot + arr[i]
            if tot>=i:
                return i
        return 0
    def hIndex(self, citations):
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)/2
            if citations[mid] >= n-mid:
                r = mid - 1
            else:
                l = mid + 1
        return n-l
