class Solution:
    def min_swaps(self, arr):
        
        result = 0

        temp = sorted(arr)
        hashmap = {}
        for index, each in enumerate(arr):
            hashmap[each] = index
        
        for index, each in enumerate(arr):
            
            if each != temp[index]:
                
                arr[index], arr[hashmap[temp[index]]] = arr[hashmap[temp[index]]], arr[index]
                
                hashmap[each] = hashmap[temp[index]]
                hashmap[temp[index]] = index
               
                result += 1
        
        return result
    
s = Solution()
arr = [10,19, 6, 3, 5]
arr = [2, 8, 5, 4]
print(s.min_swaps(arr))



