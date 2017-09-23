# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        #get the point has min y value
        import math
        minypid = 0
        for pid in range(1,len(points)):
            if points[pid].y<points[minypid].y:
                minypid = pid
        # get the move x and y
        movex = -1*points[minypid].x
        movey = -1 *points[minypid].y
        # change all point in points
        for point in points:
            point.x = point.x+movex
            point.y = point.y+movey
        # get all points jiaodu except minypid,the jiaodu value in 0-180
        jiaodu = []
        for pid in range(len(points)):
            if pid is minypid:
                jiaodu.append(360)
            else:
                bias = 0 if points[pid].x>=0 and points[pid].y>=0 else 90
                nowj = math.atan(abs(points[pid].y)*1.0/(abs(points[pid].x)+0.001))*180/3.1415
                nowj = nowj + bias
                jiaodu.append(nowj)
        stack = []
        d = {}
        print(jiaodu)
        for idx,i in enumerate(points):
            d[i] = jiaodu[idx]
        stack.append(points[minypid])
        #d = sorted(d.items(),key=lambda d:d[1])
        #points = [i[0] for i in d]
        points = sorted(points,key=lambda i:d[i])
        for i in points:
            print(i.x,i.y)
        stack.append(points[0])
        points = points[1:-1]
        def lr(point1,point2,point3):
            x1,y1 = point1.x,point1.y
            x2,y2 = point2.x,point2.y
            x3,y3 = point3.x,point3.y
            res = (x1*y2+x3*y1+x2*y3-x3*y2-x2*y1-x1*y3)
            if res>0:
                return True,abs(res)#left
            else:
                return False,abs(res)

        while len(points)!=0:
            nowpoint =points[0]
            lorr,res = lr(stack[0],stack[-1],nowpoint)
            if lorr==True or res==0:
                stack.append(nowpoint)
                points.remove(nowpoint)
            else:
                stack.pop()
        return stack
