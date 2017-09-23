class Team(object):
    def __init__(self,name):
        self.name = name
        self.jifen = 0
        self.jinshen = 0
        self.jinqiu = 0
def makedata(namelist,nlist):
    allteam = []
    name_id = {}
    for idx,i in enumerate(namelist):
        #i=='bisai'
        tmp = Team(i)
        allteam.append(tmp)
        name_id[i] = idx
    for row in nlist:
        #row-format=='name1:name2 num1:num2'
        row_nn = row.split()
        name = row_nn[0].split('-')
        score = row_nn[1].split(':')
        name1 = name[0]
        name2 = name[1]
        score1 = int(score[0])
        score2 = int(score[1])
        if score1>score2:
            allteam[name_id[name1]].jifen = allteam[name_id[name1]].jifen + 3
            allteam[name_id[name1]].jinshen = allteam[name_id[name1]].jinshen + 1
        elif score1 == score2:
            allteam[name_id[name1]].jifen = allteam[name_id[name1]].jifen + 1
            allteam[name_id[name2]].jifen = allteam[name_id[name2]].jifen + 1
        else:
            allteam[name_id[name2]].jifen = allteam[name_id[name2]].jifen + 3
            allteam[name_id[name2]].jinshen = allteam[name_id[name2]].jinshen + 1
        allteam[name_id[name1]].jinqiu = allteam[name_id[name1]].jinqiu + score1
        allteam[name_id[name2]].jinqiu = allteam[name_id[name2]].jinqiu + score2
    return allteam


def solve():
    n = int(raw_input())
    namelist = []
    nlist = []
    for i in range(n):
        namelist.append(raw_input())
    for i in range(n*(n-1)/2):
        nlist.append(raw_input())
    allteam = makedata(namelist,nlist)
    allteam = sorted(allteam,reverse=True,key=lambda i:(i.jifen,i.jinshen,i.jinqiu))
    resname = []
    for idx,i in enumerate(allteam):
        if idx==len(allteam)/2:
            break
        resname.append(i.name)
    resname.sort()
    for name in resname:
        print name
while True:
    solve()
