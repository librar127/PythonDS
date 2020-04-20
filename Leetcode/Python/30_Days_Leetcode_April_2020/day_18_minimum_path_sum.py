class Solution:
    def minPathSum(self, grid):
        
        path_list = []
        for i in range(len(grid)):
            path_list.append(grid[i])
        
        for i in range(len(path_list)):
            for j in range(len(path_list[i])):                
                if i>0 and j>0:  
                    path_list[i][j] += min(path_list[i-1][j], path_list[i][j-1])
                elif j>0: # First Row                    
                    path_list[i][j] += path_list[i][j-1]
                elif i>0: # First Column                    
                    path_list[i][j] += path_list[i-1][j]
        
        row, col = len(grid), len(grid[0])          
        return path_list[row-1][col-1]

s = Solution()
nums = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
print(s.minPathSum(nums))    