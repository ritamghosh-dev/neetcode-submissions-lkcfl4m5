class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(i, j):
            nonlocal local_visit
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            for d1, d2 in dirs:
                x, y = i+d1, j+d2
                if 0 > x or x >= m or y<0 or y>= n:
                    return False
                elif board[x][y]=="O" and (x,y) not in local_visit:
                    local_visit.add((x,y))
                    if not dfs(x,y):
                        return False
            return True
        
        visited = set()
        for i in range(m):
            for j in range(n):
                local_visit = set()
                local_visit.add((i,j))
                if board[i][j]== "O" and (i,j) not in visited:
                    visited.add((i,j))
                    if dfs(i,j):
                        for item in local_visit:
                            a, b = item[0], item[1]
                            board[a][b] = "X"
                    visited.update(local_visit)
        