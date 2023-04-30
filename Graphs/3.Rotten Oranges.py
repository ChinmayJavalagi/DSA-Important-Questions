# SC - N X M 
# TC - N X M [while] + (N X M * 4) [for] = N X M


from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        q = deque()
        visited = [[False]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append([[i,j], 0])
                    visited[i][j] = 2
                else:
                    visited[i][j] = 0
        tm = 0
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        while q:
            s = q.popleft()
            row = s[0][0]
            col = s[0][1]
            tm = max(tm, s[1])
            for i in range(4):
                nrow = row+drow[i]
                ncol = col+dcol[i]
                if nrow>=0 and nrow<r and ncol>=0 and ncol<c and visited[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                    visited[nrow][ncol] = 2
                    q.append([[nrow,ncol], s[1]+1])
        for i in range(r):
            for j in range(c):
                if visited[i][j]!=2 and grid[i][j] == 1:
                    return -1
        return tm
