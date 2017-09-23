# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def remthis(self,root,d,now):
        if root==None:
            return
        if now in d:
            tmp = d[now]
            tmp.append(root.val)
            d[now] = tmp
        else:
            d[now] = [root.val]
        now = now+1
        self.remthis(root.left,d,now+1)
        self.remthis(root.right,d,now+1)
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        now = 0
        self.remthis(root,d,0)
        res = []
        for i in range(len(d)):
            res.append(max(d[i]))
        return res
