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
                return [-1,-1]
            if a and not b:
                return [-1,-1]
            if not a and not b:
                return [0,0]
            if a.val!=b.val:
                return [-1,-1]
            l=dfs(a.left,b.left)
            r=dfs(a.right,b.right)
            if l==[-1,-1] or r==[-1,-1]:
                return [-1,-1]
            return [1+max(l[0],r[0]),1+max(l[1],r[1])]
        curr=dfs(p, q)
        if curr==[-1,-1]:
            return False
        return True


