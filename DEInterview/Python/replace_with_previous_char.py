def replaceWithPrevious(arr):
    for index in range(1, len(arr)):
        if arr[index] is None:
            arr[index] = arr[index-1]
            
            
    return arr

arr = [1,None,1,2,None] 
arr = [None, 2, None, None, 3]
print(replaceWithPrevious(arr))