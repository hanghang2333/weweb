# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxv = max(nums)
        inx = nums.index(maxv)
        tmp = TreeNode(maxv)
        tmp.left = self.constructMaximumBinaryTree(nums[0:inx])
        tmp.right = self.constructMaximumBinaryTree(nums[inx+1:])
        return tmp
