# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def recur(node):
            if not node:
                ans.append("N")
                return
            ans.append(str(node.val))
            recur(node.left)
            recur(node.right)
            return
        recur(root)
        return ','.join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ans = data.split(',')
        i=0
        def recur():
            nonlocal i
            if ans[i]=='N' or i>=len(ans):
                return None
            root = TreeNode(int(ans[i]))
            i+=1
            root.left = recur()
            i+=1
            root.right = recur()
            return root
        return recur()




