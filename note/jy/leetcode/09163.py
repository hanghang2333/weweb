def solve(timestr):
    timelist = timestr.split(':')
    h = timelist[0]
    m = timelist[1]
    s = timelist[2]
    if int(h)<=24 and int(m)<=59 and int(s)<=59:
        print(timestr)
        return
    if int(h)>24:
        #change hour
        if h[0]=='2':
            h = h[0]+'0'
        else:
            h = '0'+h[1]
    if int(m)>59:
        m = '0'+m[1]
    if int(s)>59:
        s = '0'+s[1]
    res = ':'.join([h,m,s])
    print(res)

def solution():
    n = int(raw_input())
    for i in range(n):
        timestr = raw_input()
        solve(timestr)
