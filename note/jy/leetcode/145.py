# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            now = stack.pop()
            res.add(now.val)
            if now.left!=None:
                stack.append(now.left)
            if now.right!=None:
                stack.append(now.right)
        res.reverse()
        return res
    def inorder(self,root):
        res = []
        if root==None:
            return []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
        return res
