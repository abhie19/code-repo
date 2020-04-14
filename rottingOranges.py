class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all rotten oranges
        # get neighors of an orange
        R = len(grid)
        C = len(grid[0])
        min_time = 0
        rotten = collections.deque() # doubly ended queue to remove nodes from left while appending to right
        
        def getNeighbors(r,c):
            direction = [(0,1),(1,0),(-1,0),(0,-1)]
            neighbors = []
            for d in direction:
                new_r = r+d[0]
                new_c = c+d[1]
                if new_r < R and new_r>=0 and  new_c < C and new_c>=0:
                    neighbors.append([r+d[0],c+d[1]])
            return neighbors
        
        # get all rotten nodes
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    rotten.append((r,c,min_time))
        
        # for each rotten node
        while rotten:
            r,c,min_time = rotten.popleft()
            neighbors = getNeighbors(r,c)
            for n in neighbors:
                if grid[n[0]][n[1]] == 1:
                    grid[n[0]][n[1]] = 2
                    rotten.append((n[0],n[1],min_time+1))
                    
        
        # check if any cecll in grid is 1 (fresh orange)
        if any(1 in row for row in grid): return -1
        
        return min_time
