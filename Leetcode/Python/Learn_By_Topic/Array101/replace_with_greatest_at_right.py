class Solution:
    def replaceElements(self, arr):
        n = len(arr)-1
        max_so_far = arr[n]
        arr[n] = -1
        index = n-1
        while index >= 0:
            current = arr[index]
            arr[index] = max(max_so_far, arr[index+1])
            max_so_far = max(max_so_far, current)
            index -= 1
            
        return arr
    
s =Solution()
nums = [17,18,5,4,6,1]
print(s.replaceElements(nums))