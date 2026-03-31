"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, head: Optional['Node']) -> Optional['Node']:
        if not head:
            return None
        tracker = {}
        def dfs(node, curr, visited):
            new = Node(node.val)
            nonlocal tracker
            tracker[node.val] = new
            if curr:
                new.neighbors.append(curr)
                curr.neighbors.append(new)
            prev = curr
            curr = new
            visited.add(node.val)
            for nei in node.neighbors:
                if nei.val not in visited:
                    dfs(nei, curr, visited)
                else:
                    temp = tracker[nei.val]
                    if curr not in temp.neighbors:
                        temp.neighbors.append(curr)
                    if temp not in curr.neighbors:
                        curr.neighbors.append(temp)

            return 
        dfs(head, None, set())
        return tracker[1]