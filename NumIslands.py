class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # empty grid
        if len(grid) == 0 : return 0
        
        R, C = len(grid), len(grid[0])
        # 1*1 grid
        if R * C == 1: return 1 if grid[0][0] == '1' else 0 
        
        # all other grid via DFS
        num_i = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    num_i += 1
                    self.dfs(grid, r, c)
        return num_i

    def dfs(self, grid, r, c):
        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or grid[r][c] != '1':
            return

        grid[r][c] = '0'
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for d in direction:
            self.dfs(grid, r+d[0], c+d[1])
