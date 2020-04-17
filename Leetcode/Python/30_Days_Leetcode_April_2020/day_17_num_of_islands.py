class Solution:
    
    def traverse_island(self, grid, i, j):
        
        if i < 0 or j < 0 or i>= len(grid) or j >= len(grid[i]) or grid[i][j]=='0':
            return
        else:
            #print(i, j)
            grid[i][j] = '0' 
            
            self.traverse_island(grid, i+1, j)
            self.traverse_island(grid, i-1, j)
            self.traverse_island(grid, i, j+1)
            self.traverse_island(grid, i, j-1)
            
            '''
            if grid[i+1][j] == '1':
                self.traverse_island(grid, i+1, j)            
            
            if grid[i-1][j] == '1':
                self.traverse_island(grid, i-1, j)
            
            if grid[i][j+1] == '1':            
                self.traverse_island(grid, i, j+1)
            
            if grid[i][j-1] == '1':            
                self.traverse_island(grid, i, j-1)
            '''
        
    def numIslands(self, grid):
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.traverse_island(grid, i, j)
                    count += 1
                
                #print(grid, '\n')
                #return count
        
        return count
    
s = Solution()
grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
print(s.numIslands(grid))


grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
print(s.numIslands(grid))

grid = [
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0']
]
print(s.numIslands(grid))