def rotateImage(a):
    
    size = len(a)
    
    # 1. Transpose the Array
    for row in range(size):
        for column in range(row, size):
            tmp = a[row][column]
            a[row][column] = a[column][row] 
            a[column][row] = tmp
     
    # 2. Flip the Array       
    for row in range(size):
        start_col = 0
        end_col = size-1
        
        while start_col <= end_col:
            tmp = a[row][start_col]
            a[row][start_col] = a[row][end_col]
            a[row][end_col] = tmp
            start_col += 1
            end_col -= 1
        
    return a