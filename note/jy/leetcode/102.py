# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root,d,depth):
        if root==None:
            return
        if depth in d:
            tmp = d[depth]
            tmp.append(root.val)
            d[depth] = tmp
        else:
            d[depth] = [root.val]
        if root.left!=None:
            self.dd(root.left,d,depth+1)
        if root.right!=None:
            self.dd(root.right,d,depth+1)
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        self.dd(root,d,0)
        print(d)
        res = []
        for i in range(len(d)):
            res.append(d[i])
        return res
