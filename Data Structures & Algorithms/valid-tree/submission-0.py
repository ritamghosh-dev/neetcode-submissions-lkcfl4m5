class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        graph = collections.defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        q = deque()
        q.append((0,None))
        visited = set()
        visited.add(0)
        while q:
            curr, prev = q.popleft()
            visited.add(curr)
            for adj in graph[curr]:
                if adj==prev:
                    continue
                elif adj in visited:
                    return False
                else:
                    visited.add(adj)
                    q.append((adj,curr))
        return len(visited) == n
        