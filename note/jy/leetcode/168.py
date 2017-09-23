
class Solution(object):
    def intchar(self,i):
        return chr(ord('A')+i-1)
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return 'A'
        zs = [1]
        start = 1
        while n>zs[-1]:
            #print('here')
            start = start*26
            zs.append(start)
        zs = zs[0:-1]
        zs.reverse()
        res = ''
        inx = 0
        print(zs)
        while n>0:
            print('e',n,zs[inx])
            now = n/zs[inx]
            n = n%zs[inx]
            if n==0 and inx!=len(zs)-1:
                now = now - 1
                n = zs[inx]
            if inx+1<=len(zs)-1 and n<=zs[inx+1] and n!=1:
                print(inx,n,now)
                n = now*zs[inx]+n
                inx = inx +1
                continue
            res = res + str(self.intchar(now))
            inx = inx + 1
        return res
a = Solution()
print(a.convertToTitle(701),a.convertToTitle(702))
print(a.convertToTitle(703))
