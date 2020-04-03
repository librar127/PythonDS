class Solution:
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
                 
        print(matrix)
                
s =  Solution()
input = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

input = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]
s.rotate(input)       