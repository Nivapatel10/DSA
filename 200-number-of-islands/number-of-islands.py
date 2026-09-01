from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count+=1
                    queue = deque([(r,c)])
                    visited.add((r,c))
                    while queue:
                        row,col= queue.popleft()
                        for dr,dc in directions:
                            nr = row+dr
                            nc = col+dc

                            if(0<=nr<rows and 
                               0<=nc<cols and 
                               grid[nr][nc]=="1" and 
                               (nr,nc) not in visited):
                               visited.add((nr,nc))
                               queue.append((nr,nc))
        return count       