class Solution:
    def isMonotonicArray(self, arr):
        
        return (all([True if arr[index] <= arr[index+1] else False for index in range(1, len(arr)-1)]) or \
            all([True if arr[index] >= arr[index+1] else False for index in range(1, len(arr)-1)]))
    
s = Solution()
arr = [13, 15, 17, 26, 90]
arr = [9, 7, 4, 2, 8]
print(s.isMonotonicArray(arr))