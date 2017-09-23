# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        little = min(p.val,q.val)
        big = max(p.val,q.val)
        if little <=root.val and big>=root.val:
            return root
        if big<root.val:
            return lowestCommonAncestor(root.left,p,q)
        if little>root.val:
            return lowestCommonAncestor(root.right,p,q)
