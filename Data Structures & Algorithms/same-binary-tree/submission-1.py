# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a,b):
            if not a and b:
                return False
            if a and not b:
                return False
            if not a and not b:
                return True
            if a.val!=b.val:
                return False
            l=dfs(a.left,b.left)
            r=dfs(a.right,b.right)
            if not l or not r:
                return False
            return True
        return dfs(p, q)



