def countElements(arr):
    count = 0 
    
    if len(arr) <= 1:
        return count
    
    hashset = set(arr)
    for each in arr:
        if each+1 in hashset:
            count+= 1
    return count

input = [1,2,3]
print(countElements(input))

input = [1,1,3,3,5,5,7,7]
print(countElements(input))

input = [1,3,2,3,5,0]
print(countElements(input))

input = [1,1,2,2]
print(countElements(input))