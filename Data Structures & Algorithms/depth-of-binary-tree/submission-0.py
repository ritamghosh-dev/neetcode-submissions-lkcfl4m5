# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans=-1
        def dfs(root,curr):
            self.ans=max(self.ans,curr)
            if root.left:
                dfs(root.left,curr+1)
            if root.right:
                dfs(root.right,curr+1)
            return 
        dfs(root,1)
        return self.ans
            
