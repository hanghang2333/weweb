class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people,key=lambda i:i[1])
        if len(people)<=1:
            return people
        res = [people[0]]
        tag = [1 for _ in range(len(people))]
        tag[0] = 0
        while(sum(tag)!=0):
            for i in range(1,len(people)):
                if tag[i]==1:
                    nowheight = people[i][0]
                    nowbefore = people[i][1]
                    inx = 0
                    count = 0
                    ok = False
                    if nowbefore == 0:
                        ok = True
                    else:
                        for j in range(len(res)):
                            inx = inx + 1
                            print('www',i,j,res,count,nowbefore,nowheight,res[j][0])
                            if res[j][0]>=nowheight:
                                count = count + 1
                            if count == nowbefore:
                                ok = True
                                break
                    if ok:
                        while inx<len(res) and res[inx][0]<=nowheight:
                            inx = inx + 1
                        res.insert(inx,people[i])
                        tag[i] = 0
        return res

a = Solution()
#print(a.reconstructQueue([[5,0],[4,4],[7,1],[7,0],[6,1],[5,2]]))
print(a.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
