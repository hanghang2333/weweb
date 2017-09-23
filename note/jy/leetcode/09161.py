def solve(S):
    if len(S)==0:
        return 0
    stack = []
    inx = 0
    n = len(S)
    while S[inx]=='L' and inx<=n-1:
        stack.append(S[inx])
        inx = inx + 1
    return len(stack)+1
    #inx is the first one that is R
    '''
    while inx<n-1:
        if S[inx]!=stack[-1]:
            stack.append(S[inx])
        inx = inx + 1
    count = 0
    '''
print solve('LRRLRL')
