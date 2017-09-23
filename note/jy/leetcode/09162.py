#coding=utf8
def solve(word,m,n,matrix):
    count = 0
    d = {'down':(1,0),'right':(0,1),'xie':(1,1)}
    def isvaild(i,j):
        if i>=0 and i<m and j>=0 and j<n:
            return True
        return False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                for k in d:#'down'
                    newi,newj = i,j
                    for kth in range(1,len(word)):
                        newi = newi+d[k][0]
                        newj = newj+d[k][1]
                        if isvaild(newi,newj):
                            #print(kth,i,j,matrix[newi][newj],word[kth])
                            if matrix[newi][newj]==word[kth]:
                                if kth == len(word)-1:
                                    count = count + 1
                            else:
                                break
                        else:
                            break
    print count

def solution():
    n = int(raw_input())
    for i in range(n):
        mn = raw_input()
        mnl = mn.split()
        m = int(mnl[0])
        n = int(mnl[1])
        matrix = []
        for j in range(m):
            matrix.append(raw_input())
        word = raw_input()
        solve(word,m,n,matrix)
'''
solution()
word = 'WORD'
m,n = 10,10
matrix = [
'AAAAAADROW',
'WORDBBBBBB',
'OCCCWCCCCC',
'RFFFFOFFFF',
'DHHHHHRHHH',
'ZWZVVVVDID',
'ZOZVXXDKIR',
'ZRZVXRXKIO',
'ZDZVOXXKIW',
'ZZZWXXXKIK'
]
print(solve(word,m,n,matrix))
'''
