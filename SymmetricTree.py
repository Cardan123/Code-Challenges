# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetrics(self, left: TreeNode, right: TreeNode) -> bool:
      if(left == None and right == None):
        return True
      elif (left == None or right == None):
        return False

      if(left.val != right.val):
        return False

      if(self.isSymmetrics(left.left,right.right) == False):
        return False
      
      if(self.isSymmetrics(left.right,right.left) == False):
        return False

      return True

    def isSymmetric(self, root: TreeNode) -> bool:
      if(root == None):
        return False

      return self.isSymmetrics(root.left,root.right)

root = TreeNode(1,TreeNode(2,TreeNode(3,None,None),TreeNode(4,None,None)),TreeNode(2,TreeNode(4,None,None),TreeNode(3,None,None)))

obj = Solution()
print(obj.isSymmetric(root))