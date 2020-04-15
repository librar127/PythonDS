def printTriangle(n):
    
    # number of spaces 
    k = n
  
    # outer loop to handle number of rows 
    for i in range(0, n+1): 
      
        # inner loop to handle number spaces values changing acc. to requirement 
        for _ in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns  values changing acc. to outer loop 
        for _ in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
            
printTriangle(4)