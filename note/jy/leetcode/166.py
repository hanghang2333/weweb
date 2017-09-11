class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        zs = ''
        f = False
        if numerator*denominator<0:
            f = True
        if numerator<0:
            numerator = -1*numerator
        if denominator<0:
            denominator = -1*denominator
        if numerator<denominator:
            zs = '0'
        else:
            zs = str(numerator/denominator)
        if f == True:
            zs = '-'+zs
        ys = numerator - (numerator/denominator*denominator)
        #print(ys)
        if ys == 0:
            return zs
        zs = zs+'.'
        xslist = ''
        hisys = {}
        #hisys[ys] = 0
        while ys!=0:
            if ys in hisys:
                #print(hisys,ys)
                #xunhuan start,end
                start = hisys[ys]
                end = len(xslist)
                xslist = xslist[0:start]+'('+xslist[start:]+')'
                break
            hisys[ys] = len(xslist)
            #print(hisys)
            ys = ys*10
            hisys[ys] = len(xslist)+1
            while ys<denominator:
                ys = ys * 10
                #xslist=xslist+'0'
                if ys in hisys:
                #print(hisys,ys)
                #xunhuan start,end
                    start = hisys[ys]
                    end = len(xslist)
                    xslist = xslist[0:start]+'('+xslist[start:]+')'
                    break
                xslist=xslist+'0'
                hisys[ys] = len(xslist)+1
            jg = ys/denominator
            #xslist=xslist+str(jg)
            #print(xslist)
            ys = ys-jg*denominator
            xslist=xslist+str(jg)
            if ys == 0:
                break
        return zs+xslist
a=Solution()
print a.fractionToDecimal(1,6)
print a.fractionToDecimal(1,99)
print a.fractionToDecimal(1,90)
print a.fractionToDecimal(-1,214748364)
