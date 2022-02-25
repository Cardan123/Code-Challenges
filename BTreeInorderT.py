from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def helper(self,root: TreeNode,res: List[int]):
      if(root != None):
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      res = []
      self.helper(root,res)
      return res

root = TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))
obj = Solution()
print(obj.inorderTraversal(root))