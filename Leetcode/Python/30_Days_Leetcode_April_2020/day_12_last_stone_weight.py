## Approach 1- two loops - O(N^2)
def findMax(nums):
    
    max_val = -9999
    for _, each in enumerate(nums):
        if each > max_val:
            max_val = each
            
    return max_val

def lastStoneWeight_nsquare(stones):
   
    while len(stones) > 1: # N/2 Times
        
        first = findMax(stones) 
        stones.remove(first)
        
        second = findMax(stones)
        stones.remove(second)
        
        remains = first-second
        stones.append(remains)
        
    return stones[0]
        

## Approach 2 - Using Sorting which varies from N^2 to N^2LogN and is not better than the first one.
## Approach 3 - Using MaxHeap - Complexity is NLogN - Building the Heap(NLogN) and then iterate the Loop  in O(N) times call maxHeapify two time for first and second in O(LogN).
        
nums = [2,7,4,1,8,1]
print(lastStoneWeight_nsquare(nums))

nums = [9,3,2,10]
print(lastStoneWeight_nsquare(nums))