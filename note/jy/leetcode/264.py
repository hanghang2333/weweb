class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num%2==0:
            num = num>>1
        while num%3==0:
            num = num/3
        while num%5==0:
            num = num/5
        return num==1
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #"1, 2, 3, 4, 5, 6, 8, 9, 10, 12"
        ugly = [1]
        u2,u3,u5 = 0,0,0
        while n>1:
            n2,n3,n5 = 2*ugly[u2],3*ugly[u3],5*ugly[u5]
            print(n2,n3,n5)
            minn = min((n2,n3,n5))
            if minn == n2:
                u2 = u2 + 1
            if minn == n3:
                u3 = u3 + 1
            if minn == n5:
                u5 = u5 + 1
            ugly.append(minn)
            n = n - 1
        print(ugly)
        return ugly[-1]

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        chushi = [0 for i in range(len(primes))]
        while n>1:
            res = [primes[i]*ugly[chushi[i]] for i in range(len(primes))]
            minn = min(res)
            for i in range(len(primes)):
                if minn ==res[i]:
                    chushi[i]+=1
            ugly.append(minn)
            n = n -1
        return ugly[-1]

a = Solution()
print(a.nthUglyNumber(20))
