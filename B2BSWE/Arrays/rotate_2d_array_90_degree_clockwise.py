
class Solution:
    def rotate_1(self, matrix):
        '''
        :type matrix: list of list of int
        :rtype: list of list of int
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        #result = [[0]*rows]*cols    
        result = [[None]*rows for _ in range(cols)]    
        
        for i in range(rows):
            for j in range(cols) :
              col = cols - i - 1
              result[j][col] = matrix[i][j]
        
        return result
      
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        size = len(matrix)
        
        ## Step 1 - Transpose the array
        for row in range(size):
            for column in range(row, size):
                tmp = matrix[row][column]
                matrix[row][column] = matrix[column][row] 
                matrix[column][row] = tmp
                   
        ## Flip the array          
        for row in range(size):      
            start_col = 0
            end_col = size-1
            while start_col <= end_col:
                tmp = matrix[row][start_col] 
                matrix[row][start_col] = matrix[row][end_col]
                matrix[row][end_col] = tmp
                start_col += 1
                end_col -= 1
                
        return matrix


s = Solution()
arr = [
  [ 1,  2,  3, 4],
  [ 5,  6,  7, 8],
  [ 9, 10, 11, 12],
  [13, 14, 15, 16]
]

result = s.rotate(arr)
print(result)