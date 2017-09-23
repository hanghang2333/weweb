# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root,res):
        if root==None:
            return 0
        l = self.dd(root.left)
        r = self.dd(root.right)
        res.append(abs(l-r))
        return root.val+l+r
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.dd(root,res)
        return sum(res)
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        s = [0+i.islower() for i in word]
        #print(s)
        if sum(s)==0 or sum(s)==len(word) or s[0]==0 and sum(s[1:])==len(word)-1:
            return True
        return False

class Solution1(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqn = int((n*2)**0.5-1)
        print(sqn)
        while True:
            #sprint(sqn)
            if (sqn+1)*sqn/2<=n and (sqn+1)*(sqn+2)/2>n:
                return sqn
            sqn = sqn + 1
a = Solution1()
print(a.arrangeCoins(5))
