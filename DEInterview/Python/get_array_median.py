def findMedian(arr):
    arr.sort()
    
    mid = len(arr) // 2
    if len(arr) % 2 ==0:
        return round((arr[mid-1] + arr[mid])/2, 2)
    else:
        return arr[mid]
    
arr = [4, 5, 8, 9, 10, 17] 
arr = [4, 5, 8, 9, 10] 
print(findMedian(arr))
    