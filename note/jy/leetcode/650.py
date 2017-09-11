#2 key keyboard
def yueshu(n):
    res = []
    for i in range(2,n):
        if n%i == 0:
            res.append(i)
    return res
def minSteps(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 3
    mins = n
    nowmins = n
    ylist = yueshu(n)
    for y in ylist:
        nowmins = (n-y)/y+1+minstep(y)
        mins = min(mins,nowmins)
    return mins

print(minSteps(32))
