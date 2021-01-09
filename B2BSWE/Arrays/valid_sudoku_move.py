class Solution:
    
    def validate_3x3_block(self, board, start_i, start_j):
        hashset = set()
        
        end_i = start_i + 2
        end_j = start_j + 2
        while start_i <= end_i:
            j = start_j
            while j <= end_j:
                current = board[start_i][j]
                if current == 0:
                    j += 1
                    continue
                
                if current in hashset:
                    return False
                else:
                    hashset.add(current)
                j += 1
            
            start_i += 1
            
        return True
    
    def validate_row_block(self, row):
        hashset = set()
        
        for each in row:
            if each == 0:
                continue
            if each in hashset:
                return False
            else:
                hashset.add(each)
        
        return True        
        
    def validSudoku(self, board):
        '''
        :type board: list of list of int
        :rtype: bool
        '''
        rows, cols = len(board), len(board[0])        
        isValid = True
        
        row_index = 0
        for row_index in range(rows):
            
            if not self.validate_row_block(board[row_index]):
                return False
                    
            hashset = set()
            for col_index in range(cols):
                
                # Validate each columns
                current = board[col_index][row_index]
                if current == 0:
                    continue
                
                if current in hashset:
                    return False
                else:
                    hashset.add(board[col_index][row_index])   
                    
        # Validate 3x3 grid
        block_list = [0, 1, 2]
        for i in block_list:
            for j in block_list:
                
                if not self.validate_3x3_block(board, i*3, j*3):
                    return False
                j += 1
            i += 1
                 
            
        return isValid
        
s = Solution()
input = [
         [8,3,0,0,7,0,0,0,0]
        ,[6,0,0,1,9,5,0,0,0]
        ,[0,9,8,0,0,0,0,6,0]
        ,[8,0,0,0,6,0,0,0,3]
        ,[4,0,0,8,0,3,0,0,1]
        ,[7,0,0,0,2,0,0,0,6]
        ,[0,6,0,0,0,0,2,8,0]
        ,[0,0,0,4,1,9,0,0,5]
        ,[0,0,0,0,8,0,0,7,9]
    ]
print(s.validSudoku(input))