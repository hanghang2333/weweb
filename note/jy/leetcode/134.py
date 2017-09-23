class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        res = [gas[i]-cost[i] for i in range(len(gas))]
        for i in range(len(cost)):
            start = 0
            flag = True
            for j in range(i,len(cost))+range(0,i):
                start = start + res[j]
                if start<0:
                    flag = False
                    break
            if flag:
                return i

a = Solution()
print(a.canCompleteCircuit([6,1,4,3,5],[3,8,2,4,2]))
