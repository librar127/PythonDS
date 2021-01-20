
def getTotalTime(arr):
    
    result = arr[0][1]-arr[0][0]
    arr = sorted(arr)
    print(arr)
    for index in range(1, len(arr)):
        previous = arr[index-1]
        current = arr[index]
        
        if previous[1] > current[0]:
            result += current[1]-previous[1]
        else:
            result += current[1]-current[0]
            
    
    return result


arr = [(0, 10), (13, 18), (15, 23), (21, 26)]
#arr = [(0, 10), (15, 25), (12, 20), (30, 48)]
print(getTotalTime(arr))