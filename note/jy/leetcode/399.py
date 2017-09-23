class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
        """
        d = {}
        dd = []
        def diedai(equations,values):
            #global d
            others = []
            othersvalue = []
            first = True
            for pair,value in zip(equations,values):
                if pair[0] in d:
                    d[pair[1]] = d[pair[0]]/value
                elif pair[1] in d:
                    d[pair[0]] = d[pair[1]]*value
                else:
                    if first == False:
                        others.append(pair)
                        othersvalue.append(value)
                    else:
                        #print('dd',d)
                        c = d.copy()
                        dd.append(c)
                        d.clear()
                        d[pair[1]] = 1.0
                        d[pair[0]] = d[pair[1]]*value
                        first = False
            #print(others)
            equations = others
            values = othersvalue
            if len(others)!=0:
                return True,others,othersvalue
            return False,others,othersvalue
        while(True):
            #print(equations,values)
            flag,equations,values = diedai(equations,values)
            if flag == False:
                break
        dd.append(d)
        res = []
        for pair in queries:
            flag = False
            for d in dd:
                if pair[0] in d and pair[1] in d:
                    res.append(d[pair[0]]/d[pair[1]])
                    flag = True
                    break
            if flag == False:
                res.append(-1.0)
        return res

a = Solution()
print(a.calcEquation(
[["a","b"],["c","d"],["e","f"],["g","h"]],
[4.5,2.3,8.9,0.44],
[["a","c"],["d","f"],["h","e"],["b","e"],["d","h"],["g","f"],["c","g"]]
))
