# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            elif (p.val < node.val and node.val < q.val) or (q.val < node.val and node.val < p.val):
                return node
            elif node.val == p.val or node.val == q.val:
                return node
            
            l = dfs(node.left)
            r = dfs(node.right)
            if not l and not r:
                return None
            # elif l and r:
            #     return node
            elif l:
                return l
            else:
                return r
        return dfs(root)