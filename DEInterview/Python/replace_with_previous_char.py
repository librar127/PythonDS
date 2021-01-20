def replaceWithPrevious(arr):
    for index in range(1, len(arr)):
        if arr[index] is None:
            arr[index] = arr[index-1]
            
            
    return arr

arr = [1,None,1,2,None] 
arr = [None, 2, None, None, 3]
arr = [1,None,2,3,None,None,5,None]
print(replaceWithPrevious(arr))