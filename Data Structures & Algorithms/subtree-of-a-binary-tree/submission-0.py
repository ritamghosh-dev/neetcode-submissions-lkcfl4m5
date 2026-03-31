# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def inner_dfs(a, b):
            # Both nodes are None, trees match.
            if not a and not b:
                return True
            # One is None while the other isn't, trees don't match.
            if not a or not b:
                return False
            # If values differ, trees don't match.
            if a.val != b.val:
                return False
            # Recursively check left and right subtrees.
            return inner_dfs(a.left, b.left) and inner_dfs(a.right, b.right)
        
        def dfs(node):
            if not node:
                return False
            # Check if the subtree rooted at the current node is identical to subRoot.
            if inner_dfs(node, subRoot):
                return True
            # Otherwise, recursively check left and right children.
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)