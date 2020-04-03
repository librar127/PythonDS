class Solution:
    
    def validate_row_block(self, board, row):
        
        hashset = set()
        for i in range(9):
            row_val = board[row][i]
                
            if row_val == '.':
                continue
            else:                    
                try: 
                    int_num = int(row_val)
                    if int_num > 0 and int_num < 10:
                        
                        if int_num in hashset:
                            return False
                        else:
                            hashset.add(int_num)
                        
                        continue
                    else:
                        return False
                except:
                    return False
                
        return True
    
    def validate_column_block(self, board, column):
        
        hashset = set()
        for i in range(9):
            column_val = board[i][column]
                
            if column_val == '.':
                continue
            else:                    
                try: 
                    int_num = int(column_val)
                    if int_num > 0 and int_num < 10:
                        
                        if int_num in hashset:
                            return False
                        else:
                            hashset.add(int_num)
                        
                        continue
                    else:
                        return False
                except:
                    return False
                    
        return True
            
    
    def validate_3x3_block(self, board, row, column):
        
        hashset = set()
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:                                   
                row_val = board[row+i][column+j]
                
                if row_val == '.':
                    continue
                else:                    
                    try: 
                        int_num = int(row_val)
                        if int_num > 0 and int_num < 10:
                            
                            if int_num in hashset:
                                return False
                            else:
                                hashset.add(int_num)
                            
                            continue
                        else:
                            return False
                    except:
                        return False
                    
        return True
    
    def isValidSudoku(self, board):
        
        valid = True
        row = 0        
        
        for i in range(9):
            valid = self.validate_row_block(board, i)
            if valid is False:
                return False
                        
            valid = self.validate_column_block(board, i)
            if valid is False:
                return False
        
        while row < 9:
            valid = True
            column = 0
            while column < 9:
                
                valid = self.validate_3x3_block(board, row, column)
                if valid is False:
                    return False
                column += 3
            
            row += 3
            
        return valid
            
s = Solution()
input_list1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

input_list2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

input_list3 = [
    [".",".",".",".",".",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    ["9","3",".",".","2",".","4",".","."],
    [".",".","7",".",".",".","3",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".","3","4",".",".",".","."],
    [".",".",".",".",".","3",".",".","."],
    [".",".",".",".",".","5","2",".","."]
]

print(s.isValidSudoku(input_list1))
print(s.isValidSudoku(input_list2))
print(s.isValidSudoku(input_list3))