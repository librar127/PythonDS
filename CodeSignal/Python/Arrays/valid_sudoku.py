def validate_3_x_3(grid, row_start, col_start):
    hashset = set()
    row_end = row_start+3
    col_end = col_start+3
    col_start_saved = col_start
    
    while row_start < row_end:
        col_start = col_start_saved
        while col_start < col_end:
            current_value = grid[row_start][col_start] 
            if current_value == '.':
                col_start += 1
                continue
            
            print(row_start, col_start, hashset)
            if current_value in hashset:
                return False
            else:
                hashset.add(current_value)
            col_start += 1
        row_start += 1
        
    return True            
           

def validate_row(row):
    hashset = set()
    for each in row:
        if each == '.':
            continue
            
        if each in hashset:
            return False
        else:
            hashset.add(each)
            
    return True

def sudoku2(grid):
    
    rows = 9
    columns = 9
    
    for row_index, each_row in enumerate(grid):
        
        # Validate each row
        if not validate_row(each_row):
            return False
        
        # Validate each column
        hashset = set()
        for column_index in range(columns):
            
            current_value = grid[column_index][row_index]
            if current_value == '.':
                continue
            
            if current_value in hashset:
                return False
            else:
                hashset.add(current_value)
                
    # Validate 3x3 Grid
    row_index = 0
    while row_index < rows:
        col_index = 0
        while col_index < columns:   
            print(row_index, col_index)       
            if not validate_3_x_3(grid, row_index, col_index):
                return False
            col_index += 3
        row_index += 3            
                
    return True

grid = [[".","4",".",".",".",".",".",".","."], 
        [".",".","4",".",".",".",".",".","."], 
        [".",".",".","1",".",".","7",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".","3",".",".",".","6","."], 
        [".",".",".",".",".","6",".","9","."], 
        [".",".",".",".","1",".",".",".","."], 
        [".",".",".",".",".",".","2",".","."], 
        [".",".",".","8",".",".",".",".","."]]
print(sudoku2(grid))