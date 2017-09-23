# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorder(self,root,d):
        if root == None:
            return 'null'
        nowstr = str(root.val)+','+self.postorder(root.left,d)+','+self.postorder(root.right,d)
        if nowstr in d:
            d[nowstr].append(root)
        else:
            d[nowstr]=[root]
        return nowstr
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        d = {}
        self.postorder(root,d)
        res = []
        for i in d:
            if len(d[i])>=2:
                res.append(d[i][0])
        return res

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res = sorted(list(set([i for i in j for j in matrix])))[k-1]
