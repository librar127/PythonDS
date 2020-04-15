def printPascalTriangle(numRows):

    # Initial space ate the left side
    prev = []
    current = []
    # outer loop to handle number of rows number of spaces 
    space = numRows
    result = []

    # outer loop to handle number of rows 
    for i in range(0, numRows): 

        # inner loop to handle number spaces values changing acc. to requirement 
        for _ in range(0, space): 
            print(end=" ") 

        # decrementing k after each loop 
        space = space - 1

        current = [1]*(i+1)
        current[0] = current[len(current)-1] = 1

        if i >= 2:
            for k in range(1, i):               
                current[k] = prev[k-1] + prev[k]

        result.append(current)
        prev  = current

        # inner loop to handle number of columns  values changing acc. to outer loop 
        #print(current)

        # ending line after each row 
        print(current, "\r")
    
    print('\n')
    return result

        
print(printPascalTriangle(5))