class Solution:
    
    def island_area(self, grid, i, j):
        
        if i < 0 or j < 0 or i>= len(grid) or j >= len(grid[i]) or grid[i][j]==0:
            return 0        
        else:                    
            count = 1          
            grid[i][j] = 0
        
            count += self.island_area(grid, i+1, j)
            count += self.island_area(grid, i-1, j)    
            count += self.island_area(grid, i, j+1)    
            count += self.island_area(grid, i, j-1)
            
        return count
    
    def maxAreaOfIsland(self, grid):
        if len(grid) <= 0 or len(grid) > 50:
            return 0  
        area = 0
        max_area = 0  
        for i in range(len(grid)):
            for j in range(len(grid[i])):   
                if grid[i][j] == 1:             
                    #print("i: {} - j: {}".format(i, j))
                    area = self.island_area(grid, i, j)
                
                    if area > max_area:
                        max_area = area
        return max_area               
            
    
solution = Solution()
input_list = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
# input_list = [[0,0,0,0,0,0,0,0]]
print(solution.maxAreaOfIsland(input_list))
        
