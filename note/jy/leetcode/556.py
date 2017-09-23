class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ns = [i for i in str(n)]
        maxnow = '0'
        for i in range(len(ns)-1,-1,-1):
            print(ns[i],maxnow,i)
            if ns[i]>=maxnow:
                maxnow = ns[i]
            else:
                tmp = ns[i+1:]
                tmp.sort()
                idx = 0
                if ns[i] not in tmp:
                    idx = -1
                else:
                    idx = tmp.index(ns[i])
                for k in range(idx+1,len(tmp)):
                    if tmp[k]>ns[i]:
                        idx = k
                        break
                here = tmp[idx]
                print('here',here)
                tmp = [ns[i]]+tmp[0:idx]+tmp[idx+1:]
                tmp.sort()
                print(tmp)
                ns = ns[0:i]+[here]+tmp
                break
        nsi = int(''.join(ns))
        if nsi == n or nsi>=2**32-1:
            return -1
        else:
            return nsi
a = Solution()
print(a.nextGreaterElement(19999999999))
